import json
import re
import sys
import uuid
from datetime import datetime, timedelta

import jwt
from flask import current_app, request, session
from flask_login import current_user, login_user
from peewee import JOIN, SQL, NodeList, fn
from playhouse.shortcuts import model_to_dict

from backend.database.models import (Group, Task, TaskAnswer, TaskCategory,
                                     TaskFile, TaskHint, TaskType,
                                     UserSolvedTask, User, Session)
from backend.base import CONFIG, MyMethodView, user_required, auth_user
from backend.functions import recursive_parse


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
                    TaskCategory.id, '/',
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
            class current_user:
                id = 1

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

    def get(self, task_id: str, *args, **kwargs):
        """
        Get tasks
        :param task_id: task's id
        """

        try:
            class current_user:
                id = 1

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
                    SQL('task_file_join.id IS NOT NULL'),
                    fn.CONCAT(
                        '[',
                        fn.GROUP_CONCAT(
                            fn.JSON_OBJECT(
                                'file', SQL('task_file_join.file'),
                                'size', SQL('task_file_join.size'),
                            ).distinct()
                        ).order_by(
                            SQL('task_file_join.order')
                        ),
                        ']'
                    ),
                    None
                ).alias('files'),

                fn.IF(
                    TaskHint.id.is_null(False),
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
                    TaskAnswer.id.is_null(False),
                    fn.CONCAT(
                        '[',
                        fn.GROUP_CONCAT(
                            fn.JSON_OBJECT(
                                'answer', TaskAnswer.answer,
                                'created', TaskAnswer.created,
                                'is_success', TaskAnswer.is_success
                            ).distinct()
                        ).order_by(
                            TaskAnswer.created.desc()
                        ),
                        ']'
                    ),
                    None
                ).alias('answers')

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
                    fn.CONCAT(
                        CONFIG.PATH_TO_TASK_TASK, '/',
                        TaskFile.task_id, '/files/',
                        TaskFile.file
                    ).alias('file'),
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
            ).where(
                Task.id == task_id
            ).group_by(
                Task.id
            ).dicts().first()

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
                    return {'errors': False}, 201
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
            return {'errors': True, 'message': f'{e} in {format(exc_tb.tb_lineno)}'}


class GetCurrentUserView(MyMethodView):
    decorators = [user_required]

    def get(self, *args, **kwargs):
        try:
            user = User.select(
                User.id,
                User.username,
                fn.CONCAT(
                    CONFIG.PATH_TO_USER_AVATAR, '/',
                    User.id, '/', User.avatar
                ).alias('avatar'),
                User.fio,
                User.is_blocked,
                User.is_teacher,
                User.last,
                User.online,
            ).where(
                User.id == current_user.id
            ).dicts().first()
            return {'user': user}

        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            return {'errors': True, 'message': f'{e} in {format(exc_tb.tb_lineno)}'}


class LogoutView(MyMethodView):

    def post(self, *args, **kwargs):
        session.pop('session_token')
        return {'errors': True}

    def get(self, *args, **kwargs):
        session.pop('session_token')
        return {'errors': True}
