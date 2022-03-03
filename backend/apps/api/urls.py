from backend.apps.api import views
from backend.apps.api import api

api.add_url_rule('/categories/', view_func=views.CategoriesViews.as_view('category_view'))
