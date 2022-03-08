from backend.apps.api import views
from backend.apps.api import api

api.add_url_rule('/categories/', view_func=views.CategoriesViews.as_view('category_view'))
api.add_url_rule('/categories/<category_slug>/tasks/', view_func=views.TasksViews.as_view('tasks_view'))
api.add_url_rule('/categories/<category_slug>/tasks/<task_id>/', view_func=views.TaskViews.as_view('task_view'))
api.add_url_rule('/groups/', view_func=views.GroupsVies.as_view('groups_view'))
api.add_url_rule('/tasks/answers/', view_func=views.CheckTaskAnswer.as_view('check_task_answer'))

api.add_url_rule('/users/', view_func=views.UserView.as_view('create_user'))
api.add_url_rule('/users/login/', view_func=views.LoginView.as_view('login_user'))
api.add_url_rule('/users/logout/', view_func=views.LogoutView.as_view('logout_user'))
api.add_url_rule('/users/current/', view_func=views.GetCurrentUserView.as_view('get_current_user'))
