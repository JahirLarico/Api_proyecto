from email.mime import image
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Usuario(models.Model):
    nombre_usuarios = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre_usuarios

class Perrito(models.Model):
    dueño = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="perros")
    nombre_perrito = models.CharField(max_length=50)
    raza = models.CharField(max_length=50)
    edad = models.IntegerField()
    foto = models.ImageField(upload_to='perritos')
    ult_alimentacion = models.DateField()
    def __str__(self):
        return self.nombre_perrito

class Dispositivo(models.Model):
    propietario = models.ForeignKey(Usuario, on_delete=models.CASCADE,related_name="dispositivos")
    ubicacion = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to='dispositivos')

    def __str__(self):
        return self.ubicacion
class Horario(models.Model):
    Dispo = models.ForeignKey(Dispositivo, on_delete=models.CASCADE ,related_name="horarios")
    hora = models.TimeField()
    cantidad_comida = models.IntegerField()

class City(models.Model):
    city = models.CharField(max_length=100)

    def __str__(self):
      return self.city


class Person(models.Model):
    dob = models.DateField(editable=True)
    personName = models.CharField(max_length=100)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True,related_name="personInCity")

    class Meta:
      ordering = ['-dob']

    def __str__(self):
       return self.personName