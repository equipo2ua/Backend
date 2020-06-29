from django.shortcuts import redirect, render
from django.contrib.auth.models import User, Group, GroupManager
from .models import Recolector

def crear_recolector(request, id):
    group = Group.objects.get(pk=id)
    id_group = group.id
    return render(request, "recolector/crear_recolector.html", {'id_group': id_group })

def add_recolector(request, id):
    group = Group.objects.get(pk=id)
    id_group = group.id

    if request.method == 'POST':

        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        telefono = request.POST.get('telefono')
        correo = request.POST.get('correo')
        n_documento = request.POST.get('n_documento')


        recolector_save = Recolector(
            nombre_recolector = nombre,
            apellido_recolector = apellido,
            telefono_recolector = telefono,
            correo_recolector = correo,
            n_documento_recolector = n_documento,
        )
        recolector_save.save()

        return redirect('list_main', id_group)

def editar_recolector(request, id):

    datos = Recolector.objects.get(pk=id)
    return render(request, "recolector/editar_recolector.html",{'recolector': datos})


def update_recolector(request, id):

    datos = Recolector.objects.get(pk=id)
    id_recolector = datos.id_recolector.id
    if request.method == 'POST':

        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        telefono = request.POST.get('telefono')
        correo = request.POST.get('correo')
        n_documento = request.POST.get('n_documento')

        Recolector.objects.filter(pk = id_recolector).update(
            nombre_recolector = nombre,
            apellido_recolector = apellido,
            telefono_recolector = telefono,
            correo_recolector = correo,
            n_documento_recolector = n_documento,

        )

        return redirect('lista_recolector', 3)

def lista_recolector(request, id):
    group = Group.objects.get(pk=id)
    id_group = group.id

    registros = Recolector.objects.all().order_by('-id')

    return render(request, "recolector/lista_recolector.html", {'id_group': id_group, 'registros':registros})


def bloquear(request, id):

    Recolector.objects.filter(pk=id).update(estado = 'Bloqueado')
    
    return redirect('lista_recolector', 3)


def activar(request,id):
    Recolector.objects.filter(pk=id).update(estado = 'Activo')
    
    return redirect('lista_recolector', 3)


def borrar(request, id):

    Recolector.objects.get(pk=id).delete()

    return redirect('lista_recolector', 3)
