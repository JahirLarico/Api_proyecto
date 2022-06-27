from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class HorarioSerializer(serializers.ModelSerializer):
    ubicacion = serializers.StringRelatedField(many=False)
    class Meta:
        model = Horario
        fields = ['id','hora','mensaje' ,'cantidad_comida','ubicacion']
class DispositivoSerializer(serializers.ModelSerializer):
    horarios = HorarioSerializer(many=True)
    propietario = serializers.StringRelatedField(many=False)
    class Meta:
        model = Dispositivo
        fields = ['id', 'ubicacion', 'imagen', 'propietario','horarios']
class PerritoSerializer(serializers.ModelSerializer):
    dueño = serializers.StringRelatedField(many=False)
    class Meta:
        model = Perrito
        fields = ['id', 'nombre_perrito', 'raza', 'edad', 'foto', 'ult_alimentacion','dueño']
class UserSerializer(serializers.ModelSerializer):
    perros=PerritoSerializer(many=True)
    dispositivos=DispositivoSerializer(many=True)
    class Meta:
        model = Usuario
        fields = ['id', 'nombre_usuarios', 'apellido', 'perros','dispositivos']

