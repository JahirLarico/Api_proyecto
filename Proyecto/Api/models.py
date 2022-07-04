from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Perrito(models.Model):
    dueño = models.ForeignKey(User, on_delete=models.CASCADE, related_name="perros")
    nombre = models.CharField(max_length=50)
    raza = models.CharField(max_length=50 )
    edad = models.IntegerField()
    foto = models.ImageField(upload_to='perritos', blank=True)
    def __str__(self):
        return self.nombre_perrito

class Dispositivo(models.Model):
    propietario = models.ForeignKey(User, on_delete=models.CASCADE,related_name="dispositivos")
    ubicacion = models.CharField(max_length=50 )
    nombre = models.CharField(max_length=50)
    url = models.CharField(max_length=50 , null=True)
    def __str__(self):
        return self.nombre

class Horario(models.Model):
    POCO = 'Poco'
    MASOMENOS = 'Masomenos'
    MUCHO = 'Mucho'

    CANTIDADES_CHOICES = [
        (POCO, 'Poco'),
        (MASOMENOS, 'Masomenos'),
        (MUCHO, 'Mucho'),
    ]

    Dispo = models.ForeignKey(Dispositivo, on_delete=models.CASCADE ,related_name="horarios")
    hora = models.TimeField()
    fecha = models.DateField(null=True)
    cantidad = models.CharField(max_length=50, choices=CANTIDADES_CHOICES)

