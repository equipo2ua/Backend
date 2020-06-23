
from django.conf.urls import url, include
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from administrator import views

administrator_patterns = [
    path('admin_main', views.admin_main,name="admin_main"),
    #flujo usuarios
    path('users_main', views.users_main,name="users_main"),
    path('new_user/',views.new_user, name='new_user'),
    path('user_block/',views.user_block, name='user_block'),
    path('user_activate/',views.user_activate, name='user_activate'),
    path('user_delete/',views.user_delete, name='user_delete'),
    path('edit_user/<user_id>/<page>',views.edit_user, name='edit_user'),
    path('list_main/<group_id>/',views.list_main, name='list_main'),     
    path('list_user_active/<group_id>/',views.list_user_active, name='list_user_active'),     
    path('list_user_active/<group_id>/<page>/',views.list_user_active, name='list_user_active'),     
    path('list_user_block/<group_id>/',views.list_user_block, name='list_user_block'),     
    path('list_user_block/<group_id>/<page>/',views.list_user_block, name='list_user_block'),  
    ]  
