from backend.apps.users import views
from backend.apps.users import users


# translate
users.add_url_rule('/create', view_func=views.CreateUserView.as_view('create_user'))
users.add_url_rule('/change', view_func=views.ChangedUserView.as_view('change_user'))
users.add_url_rule('/login', view_func=views.LoginView.as_view('login_user'))
users.add_url_rule('/logout', view_func=views.LogoutView.as_view('logout_user'))
users.add_url_rule('/refresh-token', view_func=views.RefreshTokenView.as_view('refresh_token'))
users.add_url_rule('/check-jwt', view_func=views.CheckJWTTokenView.as_view('check_jwt_token'))

