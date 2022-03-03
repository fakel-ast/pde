from backend.apps.api import views
from backend.apps.api import api

api.add_url_rule('/categories/', view_func=views.CategoriesViews.as_view('category_view'))
api.add_url_rule('/categories/<category_slug>/tasks/', view_func=views.TaskViews.as_view('tasks_view'))
