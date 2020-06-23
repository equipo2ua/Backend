
from django.conf.urls import url, include
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from core import views

urlpatterns = [
    path('', views.login,name="login"),
    path('check_group_main', views.check_group_main,name="check_group_main"),
    ]  
