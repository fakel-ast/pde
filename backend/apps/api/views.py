import os
import sys

from flask import json, request, abort, jsonify, current_app, render_template, Response
from peewee import fn, JOIN, SQL, CharField, NodeList
from werkzeug.exceptions import BadRequest

from backend.database.models import TaskCategory, Task
from backend.functions import recursive_parse
from backend.base import MyMethodView, CONFIG


class CategoriesViews(MyMethodView):

    def get(self, *args, **kwargs):
        """Get categories"""

        try:
            categories = TaskCategory.select(
                TaskCategory.id,
                TaskCategory.title,
                TaskCategory.created,
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
