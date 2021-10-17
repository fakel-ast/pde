from django.urls import path

from apps.users import views


urlpatterns = [
    path('sign-up/', views.SignUpView.as_view(), name='sign_up'),
    path('sign-in/', views.SignInView.as_view(), name='sign_in'),
    path('logout/', views.LogoutView.as_view(), name='user_logout'),
]


