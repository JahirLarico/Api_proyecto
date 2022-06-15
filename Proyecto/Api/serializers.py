from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class DispositivoSerializer(serializers.ModelSerializer):
    propietario = serializers.StringRelatedField(many=False)
    class Meta:
        model = Dispositivo
        fields = ['id', 'ubicacion', 'imagen', 'propietario']
class PerritoSerializer(serializers.ModelSerializer):
    nombre_usuarios = serializers.StringRelatedField(many=False)
    class Meta:
        model = Perrito
        fields = ['id', 'nombre_perrito', 'raza', 'edad', 'foto', 'ult_alimentacion','nombre_usuarios']
class UserSerializer(serializers.ModelSerializer):
    perros=PerritoSerializer(many=True)
    dispositivos=DispositivoSerializer(many=True)
    class Meta:
        model = Usuario
        fields = ['id', 'nombre_usuarios', 'apellido', 'perros','dispositivos']

class PersonSerializer(serializers.ModelSerializer):
    city = serializers.StringRelatedField(many=False)

    class Meta:
      model = Person
      fields = ("id", "personName", "dob", "city",)


class CitySerializer(serializers.ModelSerializer):
    personInCity=PersonSerializer(many=True)

    class Meta:
      model = City
      fields = ("id", "city","personInCity")

