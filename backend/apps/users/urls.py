
from django.contrib import admin
from django.urls import path, include, re_path

from apps.users import views


urlpatterns = [
    path('', views.SignUpView.as_view()),
]


