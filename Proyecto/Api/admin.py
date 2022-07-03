from django.contrib import admin

# Register your models here.


from .models import Perrito, Dispositivo, Horario, Usuario
admin.site.register(Perrito)
admin.site.register(Dispositivo)
admin.site.register(Horario)
admin.site.register(Usuario)