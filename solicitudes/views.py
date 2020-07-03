from django.shortcuts import redirect, render
from django.contrib.auth.models import User, Group, GroupManager
from .models import Solicitud
# Create your views here.

def crear_solicitud(request, id):

    return render(request, "solicitudes/crear_solicitud.html")