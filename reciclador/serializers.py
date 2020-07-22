from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Reciclador 

class RecicladorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model =Reciclador
        fields = ('nombre_reciclador','apellido_reciclador','telefono_reciclador','correo_reciclador')
