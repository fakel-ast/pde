import sys

from flask import current_app
from pydantic import ValidationError

from backend.apps.admin.schemas import CategoriesGet
from backend.database.models import (TaskCategory, )
from backend.base import MyMethodView


class CategoriesViews(MyMethodView):

    def get(self, *args, **kwargs):
        """Get categories"""

        try:
            categories = TaskCategory.select(
                TaskCategory.id,
                TaskCategory.title,
                TaskCategory.slug,
                TaskCategory.active,
            ).dicts()

            categories = list(categories)

            return {'errors': False, 'categories': categories}

        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            current_app.logger.error('Get categories: ' + format(e) + ' in ' + format(exc_tb.tb_lineno))
            return {'errors': True, 'message': 'Code error'}, 500

    def post(self, *args, **kwargs) -> dict:
        try:
            categories = CategoriesGet.parse_obj(self.data).categories
            save_categories = []
            for category_get in categories:
                print(category_get)
                category, _ = TaskCategory.get_or_create(id=category_get.id)
                category.active = category_get.active
                category.title = category_get.title
                category.slug = category_get.slug
                save_categories.append(category)
            TaskCategory.bulk_update(save_categories, fields=['active', 'title', 'slug'])
            return {'errors': False}
        except ValidationError as e:
            return e.json(), 400
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            current_app.logger.error('Save categories: ' + format(e) + ' in ' + format(exc_tb.tb_lineno))
            return {'errors': True, 'message': 'Code error'}, 500
