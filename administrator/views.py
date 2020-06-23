import calendar
import json
import random
from django.shortcuts import render
from datetime import datetime, timedelta, time
from django import forms
from django.contrib import messages
from django.core.mail import EmailMultiAlternatives
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Count, Avg, Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group, GroupManager
from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from registration.models import Profile

#admin Unab
@login_required
def admin_main(request):
    profiles = Profile.objects.get(user_id = request.user.id)
    if profiles.group_id != 1:
        messages.add_message(request, messages.INFO, 'Intenta ingresar a una area para la que no tiene permisos')
        return redirect('check_group_main')
    template_name = 'administrator/admin_main.html'
    return render(request,template_name,{'profiles':profiles})
#Flujo usuarios
@login_required
def users_main(request):
    profiles = Profile.objects.get(user_id = request.user.id)
    if profiles.group_id != 1:
        messages.add_message(request, messages.INFO, 'Intenta ingresar a una area para la que no tiene permisos')
        return redirect('check_group_main')
    groups = Group.objects.all().exclude(pk=0).exclude(pk=4).exclude(pk=6).order_by('id')
    template_name = 'administrator/users_main.html'
    return render(request,template_name,{'groups':groups,'profiles':profiles})
@login_required
def new_user(request):
    profiles = Profile.objects.get(user_id = request.user.id)
    if profiles.group_id != 1:
        messages.add_message(request, messages.INFO, 'Intenta ingresar a una area para la que no tiene permisos')
        return redirect('check_group_main')
    if request.method == 'POST':
        grupo = request.POST.get('grupo')
        rut = request.POST.get('rut')
        first_name = request.POST.get('name')
        last_name = request.POST.get('last_name1')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        rut_exist = User.objects.filter(username=rut).count()
        mail_exist = User.objects.filter(email=email).count()
        if rut_exist == 0:
            if mail_exist == 0:
                user = User.objects.create_user(
                    username= rut,
                    email=email,
                    password=rut,
                    first_name=first_name,
                    last_name=last_name,
                    )
                Profile.objects.filter(user_id = user.id).update(group_id = grupo)
                Profile.objects.filter(user_id = user.id).update(rut = rut)                
                Profile.objects.filter(user_id = user.id).update(name = first_name)
                Profile.objects.filter(user_id = user.id).update(last_name = last_name)                
                Profile.objects.filter(user_id = user.id).update(mobile = mobile)           
                messages.add_message(request, messages.INFO, 'Usuario creado con exito')                             
            else:
                messages.add_message(request, messages.INFO, 'El correo que esta tratando de ingresar, ya existe en nuestros registros')                             
        else:
            messages.add_message(request, messages.INFO, 'El rut que esta tratando de ingresar, ya existe en nuestros registros')                         
    groups = Group.objects.all().exclude(pk=0).exclude(pk=4).exclude(pk=6).order_by('id')
    template_name = 'administrator/new_user.html'
    return render(request,template_name,{'groups':groups})
@login_required
def edit_user(request,user_id,page):
    profiles = Profile.objects.get(user_id = request.user.id)
    if profiles.group_id != 1:
        messages.add_message(request, messages.INFO, 'Intenta ingresar a una area para la que no tiene permisos')
        return redirect('check_group_main')
    if request.method == 'POST':
        grupo = request.POST.get('grupo')
        user_id = request.POST.get('user_id')
        page = request.POST.get('page')
        first_name = request.POST.get('name')
        last_name = request.POST.get('last_name1')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        user_data_count = User.objects.filter(pk=user_id).count()
        user_data = User.objects.get(pk=user_id)
        profile_data = Profile.objects.get(user_id=user_id)    
        if user_data_count == 1:
            User.objects.filter(pk = user_id).update(first_name = first_name)
            User.objects.filter(pk = user_id).update(last_name = last_name)  
            User.objects.filter(pk = user_id).update(email = email)  
            Profile.objects.filter(user_id = user_id).update(name = first_name)
            Profile.objects.filter(user_id = user_id).update(last_name = last_name)  
            Profile.objects.filter(user_id = user_id).update(mobile = mobile)
            messages.add_message(request, messages.INFO, 'Usuario '+profile_data.name +' '+profile_data.last_name+' editado con éxito')                             
            return redirect('list_user_active',grupo,page)
        else:
            messages.add_message(request, messages.INFO, 'Hubo un error al editar el Usuario '+profile_data.name +' '+profile_data.last_name)
            return redirect('list_user_active',profile_data.group_id,page)    
    user_data = User.objects.get(pk=user_id)
    profile_data = Profile.objects.get(user_id=user_id)
    groups = Group.objects.get(pk=profile_data.group_id)        
    template_name = 'administrator/edit_user.html'
    return render(request,template_name,{'user_data':user_data,'profile_data':profile_data,'groups':groups,'page':page})
@login_required
def list_main(request,group_id):
    profiles = Profile.objects.get(user_id = request.user.id)
    if profiles.group_id != 1:
        messages.add_message(request, messages.INFO, 'Intenta ingresar a una area para la que no tiene permisos')
        return redirect('check_group_main')
    group = Group.objects.get(pk=group_id)
    template_name = 'administrator/list_main.html'
    return render(request,template_name,{'group':group,'profiles':profiles})
@login_required    
def list_user_active(request,group_id,page=None):
    profiles = Profile.objects.get(user_id = request.user.id)
    if profiles.group_id != 1:
        messages.add_message(request, messages.INFO, 'Intenta ingresar a una area para la que no tiene permisos')
        return redirect('check_group_main')
    if page == None:
        page = request.GET.get('page')
    else:
        page = page
    if request.GET.get('page') == None:
        page = page
    else:
        page = request.GET.get('page')
    group = Group.objects.get(pk=group_id)
    user_all = []
    user_array = User.objects.filter(is_active='t').filter(profile__group_id=group_id).order_by('first_name')
    for us in user_array:
        profile_data = Profile.objects.get(user_id=us.id)
        name = us.first_name+' '+us.last_name
        user_all.append({'id':us.id,'user_name':us.username,'name':name,'mobile':profile_data.mobile,'mail':us.email})
    paginator = Paginator(user_all, 30)  
    user_list = paginator.get_page(page)
    template_name = 'administrator/list_user_active.html'
    return render(request,template_name,{'profiles':profiles,'group':group,'user_list':user_list,'paginator':paginator,'page':page})
@login_required    
def list_user_block(request,group_id,page=None):
    profiles = Profile.objects.get(user_id = request.user.id)
    if profiles.group_id != 1:
        messages.add_message(request, messages.INFO, 'Intenta ingresar a una area para la que no tiene permisos')
        return redirect('check_group_main')
    if page == None:
        page = request.GET.get('page')
    else:
        page = page
    if request.GET.get('page') == None:
        page = page
    else:
        page = request.GET.get('page')
    group = Group.objects.get(pk=group_id)
    user_all = []
    user_array = User.objects.filter(is_active='f').filter(profile__group_id=group_id).order_by('first_name')
    for us in user_array:
        profile_data = Profile.objects.get(user_id=us.id)
        name = us.first_name+' '+us.last_name
        user_all.append({'id':us.id,'user_name':us.username,'name':name,'mobile':profile_data.mobile,'mail':us.email})
    paginator = Paginator(user_all, 30)  
    user_list = paginator.get_page(page)
    template_name = 'administrator/list_user_block.html'
    return render(request,template_name,{'profiles':profiles,'group':group,'user_list':user_list,'paginator':paginator,'page':page})
@login_required
def user_block(request):
    profiles = Profile.objects.get(user_id = request.user.id)
    if profiles.group_id != 1:
        messages.add_message(request, messages.INFO, 'Intenta ingresar a una area para la que no tiene permisos')
        return redirect('check_group_main')
    if request.method == 'POST':
        user_id = request.POST.get('u_id')
        page = request.POST.get('page')
        user_data_count = User.objects.filter(pk=user_id).count()
        user_data = User.objects.get(pk=user_id)
        profile_data = Profile.objects.get(user_id=user_id)       
        if user_data_count == 1:
            User.objects.filter(pk=user_id).update(is_active='f')
            messages.add_message(request, messages.INFO, 'Usuario '+profile_data.name +' '+profile_data.last_name+' bloqueado con éxito')
            return redirect('list_user_active',profile_data.group_id,page)        
        else:
            messages.add_message(request, messages.INFO, 'Hubo un error al bloquear el Usuario '+profile_data.name +' '+profile_data.last_name)
            return redirect('list_user_active',profile_data.group_id,page)        
    else:
        messages.add_message(request, messages.INFO, 'Hubo un error al editar un usuario, intentelo nuevamente')
        return redirect('check_group_main')
@login_required
def user_activate(request):
    profiles = Profile.objects.get(user_id = request.user.id)
    if profiles.group_id != 1:
        messages.add_message(request, messages.INFO, 'Intenta ingresar a una area para la que no tiene permisos')
        return redirect('check_group_main')
    if request.method == 'POST':
        user_id = request.POST.get('u_id')
        page = request.POST.get('page')
        user_data_count = User.objects.filter(pk=user_id).count()
        user_data = User.objects.get(pk=user_id)
        profile_data = Profile.objects.get(user_id=user_id)       
        if user_data_count == 1:
            User.objects.filter(pk=user_id).update(is_active='t')
            messages.add_message(request, messages.INFO, 'Usuario '+profile_data.name +' '+profile_data.last_name+' activado con éxito')
            return redirect('list_user_block',profile_data.group_id,page)        
        else:
            messages.add_message(request, messages.INFO, 'Hubo un error al activar el Usuario '+profile_data.name +' '+profile_data.last_name)
            return redirect('list_user_block',profile_data.group_id,page)        
    else:
        messages.add_message(request, messages.INFO, 'Hubo un error al editar un usuario, intentelo nuevamente')
        return redirect('check_group_main')
@login_required
def user_delete(request):
    profiles = Profile.objects.get(user_id = request.user.id)
    if profiles.group_id != 1:
        messages.add_message(request, messages.INFO, 'Intenta ingresar a una area para la que no tiene permisos')
        return redirect('check_group_main')
    if request.method == 'POST':
        user_id = request.POST.get('u_id')
        page = request.POST.get('page')
        user_data_count = User.objects.filter(pk=user_id).count()
        user_data = User.objects.get(pk=user_id)
        profile_data = Profile.objects.get(user_id=user_id)       
        if user_data_count == 1:
            password_delete = random.randint(10000, 99999)
            Profile.objects.filter(user_id=user_id).delete()
            User.objects.filter(pk=user_id).update(is_active='f')
            User.objects.filter(pk=user_id).update(username=user_id)
            User.objects.filter(pk=user_id).update(password=password_delete)
            messages.add_message(request, messages.INFO, 'Usuario '+profile_data.name +' '+profile_data.last_name+' eliminado con éxito')
            return redirect('list_user_block',profile_data.group_id,page)        
        else:
            messages.add_message(request, messages.INFO, 'Hubo un error al eliminar el Usuario '+profile_data.name +' '+profile_data.last_name)
            return redirect('list_user_block',profile_data.group_id,page)        
    else:
        messages.add_message(request, messages.INFO, 'Hubo un error al editar un usuario, intentelo nuevamente')
        return redirect('check_group_main')
