import calendar
import json
from datetime import datetime, timedelta, time
from django import forms
from django.contrib import messages
from django.core.mail import EmailMultiAlternatives
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group, GroupManager
from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from registration.models import Profile

#flow login
def login(request):
    return redirect('accounts/login/')
@login_required
def check_group_main(request):
    profiles = Profile.objects.get(user_id = request.user.id)
    if profiles.group_id == 1:  
        return redirect('admin_main')   
    return redirect('logout')
#end flow login
