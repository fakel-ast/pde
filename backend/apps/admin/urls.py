from backend.apps.admin import views
from backend.apps.admin import admin

admin.add_url_rule('categories/', view_func=views.CategoriesViews.as_view('category_view'))

