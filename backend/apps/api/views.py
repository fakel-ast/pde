import os
import sys

from flask import json, request, abort, jsonify, current_app, render_template, Response
from peewee import fn, JOIN, SQL, CharField, NodeList
from werkzeug.exceptions import BadRequest

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


class TaskViews(MyMethodView):

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
