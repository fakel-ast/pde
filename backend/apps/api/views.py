import os
import sys

from flask import json, request, abort, jsonify, current_app, render_template, Response
from peewee import fn, JOIN, SQL, CharField, NodeList
from flask_login import current_user

from backend.database.models import TaskCategory, Task, TaskType, TaskAnswer, TaskFile, TaskHint, UserSolvedTask
from backend.functions import recursive_parse
from backend.base import MyMethodView, CONFIG


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
