import json
import re
import sys
import uuid
from datetime import datetime, timedelta

import jwt
from flask import current_app, request, session, abort
from flask_login import current_user, login_user
from peewee import JOIN, SQL, NodeList, fn
from playhouse.shortcuts import model_to_dict
from werkzeug.exceptions import BadRequest

from backend.database.models import (Group, Task, TaskAnswer, TaskCategory,
                                     TaskFile, TaskHint, TaskType,
                                     UserSolvedTask, User, Session, TaskTextAnswer)
from backend.base import CONFIG, MyMethodView, user_required, auth_user
from backend.functions import recursive_parse, get_current_user


class CategoriesViews(MyMethodView):

    def get(self, *args, **kwargs):
        """Get categories"""

        try:
            categories = TaskCategory.select(
                TaskCategory.id,
                TaskCategory.title,
                TaskCategory.slug,
                fn.CONCAT(
                    CONFIG.PATH_TO_TASK_CATEGORIES_IMAGES, '/',
                    TaskCategory.image
                ),
                fn.COUNT(Task.id.distinct()).alias('tasks_count')
            ).join(
                Task,
                JOIN.LEFT_OUTER
            ).where(
                TaskCategory.active
            ).group_by(
                TaskCategory.id
            ).dicts()

            categories = recursive_parse(list(categories))

            return {'errors': False, 'categories': categories}

        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            current_app.logger.error('Get categories: ' + format(e) + ' in ' + format(exc_tb.tb_lineno))
            return {'errors': True, 'message': 'Code error'}, 500


class TasksViews(MyMethodView):

    def get(self, category_slug: str, *args, **kwargs):
        """
        Get tasks
        :param category_slug: slug TaskCategory
        """

        try:
            tasks = Task.select(
                Task.id,
                Task.created,
                Task.title,
                Task.point_count,
                fn.COUNT(UserSolvedTask.id.distinct()).alias('solved_count'),
                fn.JSON_CONTAINS(fn.JSON_ARRAYAGG(UserSolvedTask.user_id), str(current_user.id)).alias('is_solved'),
            ).join(
                TaskCategory
            ).join_from(
                Task,
                UserSolvedTask,
                JOIN.LEFT_OUTER,
                on=(Task.id == UserSolvedTask.task_id)
            ).where(
                TaskCategory.slug == category_slug
            ).group_by(
                Task.id
            ).dicts()

            tasks = recursive_parse(list(tasks))

            return {'errors': False, 'tasks': tasks}

        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            current_app.logger.error('Get categories: ' + format(e) + ' in ' + format(exc_tb.tb_lineno))
            return {'errors': True, 'message': 'Code error'}, 500


class TaskViews(MyMethodView):

    def get(self, task_id: str, category_slug: str, *args, **kwargs):
        """
        Get tasks
        :param task_id: task's id
        :param category_slug: slug TaskCategory
        """

        try:
            task = Task.select(
                Task.id,
                Task.created,
                Task.title,
                Task.point_count,
                Task.description,
                TaskType.title.alias('type'),
                fn.COUNT(UserSolvedTask.id.distinct()).alias('solved_count'),
                fn.JSON_CONTAINS(fn.JSON_ARRAYAGG(UserSolvedTask.user_id), str(current_user.id)).alias('is_solved'),

                fn.IF(
                    SQL('COUNT(task_file_join.id) != 0'),
                    fn.CONCAT(
                        '[',
                        fn.GROUP_CONCAT(
                            fn.JSON_OBJECT(
                                'file_link', SQL('task_file_join.file_link'),
                                'file', SQL('task_file_join.file'),
                                'size', SQL('task_file_join.size'),
                                'id', SQL('task_file_join.id')
                            ).distinct()
                        ).order_by(
                            SQL('task_file_join.order')
                        ),
                        ']'
                    ),
                    None
                ).alias('files'),

                fn.IF(
                    fn.COUNT(TaskHint.id) != 0,
                    fn.CONCAT(
                        '[',
                        fn.GROUP_CONCAT(
                            fn.JSON_OBJECT(
                                'text', TaskHint.hint,
                            ).distinct()
                        ).order_by(
                            TaskHint.order
                        ),
                        ']'
                    ),
                    None
                ).alias('hints'),

                fn.IF(
                    fn.COUNT(TaskAnswer.id) != 0,
                    fn.CONCAT(
                        '[',
                        fn.GROUP_CONCAT(
                            fn.JSON_OBJECT(
                                'answer', TaskAnswer.answer,
                                'created', TaskAnswer.created,
                                'is_success', TaskAnswer.is_success,
                                'id', TaskAnswer.id
                            ).distinct()
                        ).order_by(
                            TaskAnswer.created.desc()
                        ),
                        ']'
                    ),
                    None
                ).alias('answers'),

                SQL('IFNULL(success_answers.count, 0)').alias('success_answers_count'),
                SQL('IFNULL(wrong_answers.count, 0)').alias('wrong_answers_count'),
                SQL('IFNULL(wrong_answers.count, 0) + IFNULL(success_answers.count, 0)').alias('all_answers'),

            ).join_from(
                Task,
                UserSolvedTask,
                JOIN.LEFT_OUTER,
                on=(Task.id == UserSolvedTask.task_id)
            ).join(
                TaskFile.select(
                    TaskFile.id,
                    TaskFile.task_id,
                    TaskFile.order,
                    TaskFile.size,
                    TaskFile.file.alias('file'),
                    fn.CONCAT(
                        CONFIG.PATH_TO_TASK_TASK, '/',
                        TaskFile.task_id, '/',
                        TaskFile.file
                    ).alias('file_link'),
                ).alias('task_file_join'),
                JOIN.LEFT_OUTER,
                on=(Task.id == SQL('task_file_join.task_id'))
            ).join_from(
                Task,
                TaskHint,
                JOIN.LEFT_OUTER
            ).join_from(
                Task,
                TaskAnswer,
                JOIN.LEFT_OUTER,
                on=((Task.id == TaskAnswer.task_id) & (current_user.id == TaskAnswer.user_id))
            ).join_from(
                Task,
                TaskType
            ).join_from(
                Task,
                TaskCategory
            ).join(
                TaskAnswer.select(
                    TaskAnswer.task_id,
                    fn.COUNT(TaskAnswer.id).alias('count')
                ).where(
                    TaskAnswer.is_success
                ).group_by(
                    TaskAnswer.task_id
                ).alias('success_answers'),
                JOIN.LEFT_OUTER,
                on=(SQL('success_answers.task_id') == Task.id)
            ).join(
                TaskAnswer.select(
                    TaskAnswer.task_id,
                    fn.COUNT(TaskAnswer.id).alias('count')
                ).where(
                    TaskAnswer.is_success == 0
                ).group_by(
                    TaskAnswer.task_id
                ).alias('wrong_answers'),
                JOIN.LEFT_OUTER,
                on=(SQL('wrong_answers.task_id') == Task.id)
            ).where(
                Task.id == task_id, TaskCategory.slug == category_slug
            ).group_by(
                Task.id
            ).dicts().first()

            if not task:
                return {'errors': True, 'message': 'Not valid task\'s id'}, 404

            task = recursive_parse(task)

            return {'errors': False, 'task': task}

        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            current_app.logger.error('Get categories: ' + format(e) + ' in ' + format(exc_tb.tb_lineno))
            return {'errors': True, 'message': 'Code error'}, 500


class UserView(MyMethodView):

    def post(self, *args, **kwargs):
        try:
            if self.data.get('password') and self.data.get('username') and \
                    self.data.get('group') and self.data.get('email'):

                group = Group.get_or_none(id=self.data.get('group'))
                if not group:
                    return {'errors': True, 'msg': 'Not valid group\'s id'}, 400

                password = self.data.get('password') or ''
                username = self.data.get('username') or ''

                if not re.search(r'(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])[0-9a-zA-Z!@#$%^&*]{6,}', password):
                    return {'errors': True, 'msg': 'Bad password'}, 400
                if User.get_or_none(username=username):
                    return {'errors': True, 'msg': 'Username already use'}, 400

                user = User()
                user.create_user(
                    password=self.data.get('password'),
                    username=self.data.get('username'),
                    email=self.data.get('email')
                )
                user.group = group
                user.save()
                if user:
                    auth_user(user=user)
                    return {'errors': False, 'user': model_to_dict(user)}, 201
            return {'errors': True, 'message': 'Not valid data'}, 400
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            current_app.logger.error('Create user: ' + format(e) + ' in ' + format(exc_tb.tb_lineno))
            return {'errors': True, 'message': 'code error'}, 500

    def get(self, *args, **kwargs):
        """Check exists username"""
        try:
            username = request.args.get('username')
            return {'is_exists': User.select().where(User.username == username).exists()}

        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            current_app.logger.error('Get user: ' + format(e) + ' in ' + format(exc_tb.tb_lineno))
            return {'errors': True, 'message': 'code error'}, 500


class LoginView(MyMethodView):

    def post(self, *args, **kwargs):
        try:

            user = User.select().where(User.username == self.data.get('username', '')).first()
            if user and user.check_password(self.data.get('password', '')):
                return auth_user(user=user)
            return {'errors': True, 'message': 'Not valid data'}, 400

        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            current_app.logger.error('Login: ' + format(e) + ' in ' + format(exc_tb.tb_lineno))
            return {'errors': True, 'message': 'Code error'}, 500


class GetCurrentUserView(MyMethodView):
    decorators = [user_required]

    def get(self, *args, **kwargs):
        try:
            return {'errors': False, 'user': get_current_user()}

        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            current_app.logger.error('Get current user: ' + format(e) + ' in ' + format(exc_tb.tb_lineno))
            return {'errors': True, 'message': 'Code error'}, 500


class LogoutView(MyMethodView):

    def post(self, *args, **kwargs):
        if 'session_token' in session:
            session.pop('session_token')
        return {'errors': True}

    def get(self, *args, **kwargs):
        if 'session_token' in session:
            session.pop('session_token')
        return {'errors': True}


class GroupsVies(MyMethodView):

    def get(self, *args, **kwargs):
        try:
            groups = Group.select(
                Group.id,
                Group.short_title.alias('title'),
                Group.full_title.alias('full_title'),
            ).where(
                Group.id
            ).order_by(
                Group.order
            ).dicts()

            return {'errors': False, 'groups': list(groups)}

        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            current_app.logger.error('Get groups: ' + format(e) + ' in ' + format(exc_tb.tb_lineno))
            return {'errors': True, 'message': 'Code error'}, 500


class CheckTaskAnswer(MyMethodView):
    """Views for check task's success answer"""
    decorators = [user_required]

    def post(self, *args, **kwargs):

        try:
            self.schema = {
                "type": "object",
                "properties": {
                    "answer": {"pattern": r"^.{0,512}$"},
                    "task": {"type": "number", "pattern": r"^[\d]{1,11}$"},
                },
                "additionalProperties": False,
                "required": ["task", "answer"]
            }

            super(CheckTaskAnswer, self).post(*args, **kwargs)

            task_id = self.data.get('task', 0)
            answer_for_test = self.data.get('answer', '')
            is_success_answer = False
            data_answer = {}

            task = Task.select(
                Task.id,
                TaskTextAnswer.answer,
                TaskType.title.alias('type_title'),
            ).join(
                TaskType
            ).join_from(
                Task,
                TaskTextAnswer,
                JOIN.LEFT_OUTER
            ).where(
                Task.id == task_id
            ).objects().first()

            if not task:
                return {'errors': True, 'message': 'Not valid task\'s id'}, 404

            if task.type_title == 'text_answer':
                # Check on true correct answer
                is_success_answer = answer_for_test == task.answer
                answer = TaskAnswer.create(
                    task_id=task_id,
                    user=current_user.id,
                    answer=answer_for_test,
                    is_success=is_success_answer,
                )
                # create data for front
                data_answer = {
                    'answer': answer.answer,
                    'created': answer.created,
                    'id': answer.id,
                    'is_success': answer.is_success
                }

                # if task is resolved save it in UserSolvedTask
                if is_success_answer:
                    UserSolvedTask.create(
                        user_id=current_user.id,
                        task_id=task_id
                    )
            return {'errors': False, 'is_success': is_success_answer, 'new_answer': data_answer}

        except BadRequest as e:
            abort(e.code)
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            current_app.logger.error('Save answer: ' + format(e) + ' in ' + format(exc_tb.tb_lineno))
            return {'errors': True, 'message': 'Code error'}, 500
