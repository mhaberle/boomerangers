from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path, re_path

from . import views

urlpatterns = [
	path('createboomerang/', views.create_boomerang, name='create_boomerang'),
	path('get_started/', views.get_started, name='get_started'),
	path('view/', views.user_profile, name='user_profile'),
	path('edit/', views.edit_user_profile, name='edit_user_profile'),
]
