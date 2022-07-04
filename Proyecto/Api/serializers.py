from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class HorarioSerializer(serializers.ModelSerializer):
    Dispo_id = serializers.StringRelatedField(many=False)
    class Meta:
        model = Horario
        fields = ['id','hora','fecha' ,'cantidad_comida','Dispo_id']
    def create(self, validated_data):
        return Horario.objects.create(**validated_data)
    
class DispositivoSerializer(serializers.ModelSerializer):
    horarios = HorarioSerializer(many=True)
    #propietario = serializers.StringRelatedField(many=False)
    class Meta:
        model = Dispositivo
        fields = ['id', 'nombre', 'ubicacion', 'url_conexion','propietario','horarios']
    def create(self, validated_data):
        horarios_data = validated_data.pop('horarios')
        dispositivo = Dispositivo.objects.create(**validated_data)
        return dispositivo
    def update(self, instance, validated_data):
        instance.nombre = validated_data.get('nombre', instance.nombre)
        instance.ubicacion = validated_data.get('ubicacion', instance.ubicacion)
        instance.url_conexion = validated_data.get('url_conexion', instance.url_conexion)
        instance.propietario = validated_data.get('propietario', instance.propietario)
        instance.save()
        return instance
    def __init__(self, *args, **kwargs):
        super(DispositivoSerializer, self).__init__(*args, **kwargs)
        self.fields['horarios'].required = False
class PerritoSerializer(serializers.ModelSerializer):
    #dueño = serializers.StringRelatedField(many=False)
    class Meta:
        model = Perrito
        fields = ['id', 'foto','nombre_perrito', 'raza', 'edad','dueño']
class UserSerializer(serializers.ModelSerializer):
    #perros=PerritoSerializer(many=True)
    #dispositivos=DispositivoSerializer(many=True)
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'perros','dispositivos']
    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            password=validated_data['password'],
        )
        return user
    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.set_password(validated_data.get('password', instance.password))
        instance.save()
        return instance
    
