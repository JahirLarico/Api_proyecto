from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser
# Create your models here.


class Usuario(models.Model):
    nombre_usuarios = models.CharField(max_length=50 , default='a')
    apellido = models.CharField(max_length=50 ,default='b')
    def apellido (self):
        self.apellido = str(self.apellido)
        return make_password(self.apellido)
    def __str__(self):
        return self.nombre_usuarios

class Perrito(models.Model):
    dueño = models.ForeignKey(User, on_delete=models.CASCADE, related_name="perros")
    nombre_perrito = models.CharField(max_length=50)
    raza = models.CharField(max_length=50 , default="asd")
    edad = models.IntegerField()
    foto = models.CharField(max_length=50)
    ult_alimentacion = models.CharField(max_length=50 , default="asd")

    def __str__(self):
        return self.nombre_perrito

class Dispositivo(models.Model):
    propietario = models.ForeignKey(User, on_delete=models.CASCADE,related_name="dispositivos")
    ubicacion = models.CharField(max_length=50 , default="Cocina")
    imagen = models.CharField(max_length=50)
    def __str__(self):
        return self.ubicacion

class Horario(models.Model):
    Dispo = models.ForeignKey(Dispositivo, on_delete=models.CASCADE ,related_name="horarios")
    mensaje = models.CharField(max_length=50, default="JAMPIOIIIIII")
    hora = models.TimeField()
    cantidad_comida = models.IntegerField()

