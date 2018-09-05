from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path, re_path

from . import views

urlpatterns = [
	path('view/', views.user_profile, name='edit_user_profile'),
	path('edit/', views.edit_user_profile, name='edit_user_profile'),
]
