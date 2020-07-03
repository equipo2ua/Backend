from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group, GroupManager
from .models import Reciclador, Comuna, Direccion, Reciclador_Direccion
# Create your views here.

def crear_reciclador(request, id):
    group = Group.objects.get(pk=id)
    id_group = group.id
    return render(request, "reciclador/crear_reciclador.html", {'id_group': id_group })

def add_reciclador(request, id):
    group = Group.objects.get(pk=id)
    id_group = group.id

    if request.method == 'POST':

        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        telefono = request.POST.get('telefono')
        correo = request.POST.get('correo')
        calle = request.POST.get('calle')
        comuna = request.POST.get('comuna')

        reciclador_save = Reciclador(
            nombre_reciclador = nombre,
            apellido_reciclador = apellido,
            telefono_reciclador = telefono,
            correo_reciclador = correo,
        )
        reciclador_save.save()

        comuna_save = Comuna(
            nombre_comuna = comuna,
        )
        comuna_save.save()

        calle_save = Direccion(
            calle_direccion = calle,
            id_comuna = comuna_save,
        )
        calle_save.save()

        rec_dir_save = Reciclador_Direccion(
            id_reciclador = reciclador_save,
            id_direccion = calle_save,
        )
        rec_dir_save.save()  

        return redirect('list_main', id_group)

def editar_reciclador(request, id):

    reciclador = Reciclador.objects.get(pk=id)
    direccion = Reciclador_Direccion.objects.filter(id_reciclador=reciclador.id)
   
    return render(request, "reciclador/editar_reciclador.html",{'reciclador': reciclador, 'direccion': direccion})

def update_reciclador(request, id):

    reciclador = Reciclador.objects.get(pk=id)

    id_reciclador = reciclador.id

    nombre = request.POST.get('nombre')
    apellido = request.POST.get('apellido')
    telefono = request.POST.get('telefono')
    correo = request.POST.get('correo')
   

    Reciclador.objects.filter(pk = id_reciclador).update(
        nombre_reciclador = nombre,
        apellido_reciclador = apellido,
        telefono_reciclador = telefono,
        correo_reciclador = correo,
    )
    
    return redirect('lista_reciclador', 2)

def lista_reciclador(request, id):
    group = Group.objects.get(pk=id)
    id_group = group.id

    registros = Reciclador.objects.all().order_by('-id')

    return render(request, "reciclador/lista_reciclador.html", {'id_group': id_group, 'registros':registros})

def bloquear(request, id):

    Reciclador.objects.filter(pk=id).update(estado = 'Bloqueado')
    
    return redirect('lista_reciclador', 2)

def activar(request,id):
    Reciclador.objects.filter(pk=id).update(estado = 'Activo')
    
    return redirect('lista_reciclador', 2)

def borrar(request, id):
    reciclador = Reciclador.objects.get(pk=id)
    id_reciclador = reciclador.id
    intermedia = Reciclador_Direccion.objects.all()
    
    for a in intermedia:
        if a.id_reciclador == reciclador:
            Comuna.objects.filter(id = a.id_direccion.id_comuna.id).delete() 
    Reciclador.objects.filter(id = id_reciclador).delete()
    return redirect('lista_reciclador', 2)

def ver_reciclador(request, id):

    reciclador = Reciclador.objects.get(pk=id)
    direcciones = Reciclador_Direccion.objects.filter(id_reciclador=reciclador.id)
    
    return render(request, "reciclador/ver_reciclador.html", {'reciclador':reciclador,'direcciones':direcciones})

def guardar_direccion(request, id):

    reciclador = Reciclador.objects.get(pk=id)
    direcciones = Reciclador_Direccion.objects.filter(id_reciclador=reciclador.id)

    calle = request.POST.get('calle')
    comuna = request.POST.get('comuna')

    if request.method == 'POST':

        comuna_save = Comuna(
            nombre_comuna = comuna,
        )
        comuna_save.save()

        calle_save = Direccion(
            calle_direccion = calle,
            id_comuna = comuna_save,
        )
        calle_save.save()

        rec_dir_save = Reciclador_Direccion(
            id_reciclador = reciclador,
            id_direccion = calle_save,
            )
        rec_dir_save.save()  

        return render(request, "reciclador/ver_reciclador.html", {'reciclador':reciclador,'direcciones':direcciones})

def borrar_direccion(request, id):
    direccion = Direccion.objects.get(pk=id)
    intermedia = Reciclador_Direccion.objects.get(id_direccion = direccion.id)

    reciclador = Reciclador.objects.get(pk=intermedia.id_reciclador.id)
    direcciones = Reciclador_Direccion.objects.filter(id_reciclador=reciclador.id)

    

    comuna = direccion.id_comuna.id
    Comuna.objects.filter(id = comuna).delete() 

    return render(request, "reciclador/ver_reciclador.html", {'reciclador':reciclador,'direcciones':direcciones})         