from ast import Delete
from re import A
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import *
from .serializers import *


class IndexView(APIView):
    def get(self,request):
        context = {
            'mensaje' :'servidor activo'
        }
        return Response(context)



class UserList(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class UserDetail(APIView):
    def get(self, request):
        username = request.GET.get('username', '')
        user = User.objects.get(username=username)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    def put(self, request):
        username = request.GET.get('username', '')
        user = User.objects.get(username=username)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    def delete(self, request):
        username = request.GET.get('username', '')
        user = User.objects.get(username=username)
        user.delete()
        return Response(status=204)

class PerritoList(APIView):
    def get(self, request):
        perritos = Perrito.objects.all()
        serializer = PerritoSerializer(perritos, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = PerritoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class PerritosByUser(APIView):
    def get(self, request):
        id=request.GET.get('idDueno', '')
        perritos = Perrito.objects.filter(dueño=id)
        serializer = PerritoSerializer(perritos , many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = PerritoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class PerritoEdit(APIView):
    def get(self, request):
        idDueno= request.GET.get('idDueno', '')
        idPerro= request.GET.get('idPerro', '')
        perritos = Perrito.objects.get(id=idPerro, dueño_id=idDueno)
        serializer = PerritoSerializer(perritos)
        return Response(serializer.data)
    def put(self, request):
        idDueno= request.GET.get('idDueno', '')
        idPerro= request.GET.get('idPerro', '')
        perritos = Perrito.objects.get(id=idPerro, dueño_id=idDueno)
        serializer = PerritoSerializer(perritos, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    def delete(self, request):
        idDueno= request.GET.get('idDueno', '')
        idPerro= request.GET.get('idPerro', '')
        perritos = Perrito.objects.get(id=idPerro, dueño_id=idDueno)
        perritos.delete()
        return Response(status=204)

class PerritoByNameInUsuarioList(APIView):
    def get(self, request):
        id=request.GET.get('id', '')
        name = request.GET.get('nombre_perrito', '')
        perritos = Perrito.objects.filter(dueño_id=id, nombre_perrito=name)
        serializer = PerritoSerializer(perritos, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = DispositivoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    def delete(self, request):
        id=request.GET.get('id', '')
        name = request.GET.get('nombre_perrito', '')
        perritos = Perrito.objects.get(dueño_id=id, nombre_perrito=name)
        perritos.delete()
        return Response(status=204)

class DispositivoList(APIView):
    def get(self, request):
        dispositivos = Dispositivo.objects.all()
        serializer = DispositivoSerializer(dispositivos, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = DispositivoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
class DispositivoByUser(APIView):
    def get(self, request):
        id=request.GET.get('userId', '')
        dispositivos = Dispositivo.objects.filter(propietario_id=id)
        serializer = DispositivoSerializer(dispositivos, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = DispositivoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class DispositivoEdit(APIView):
    def get(self, request):
        userId= request.GET.get('idDueno', '')
        dispoId= request.GET.get('idDispo', '')
        dispositivos = Dispositivo.objects.get(id=dispoId, propietario_id=userId)
        serializer = DispositivoSerializer(dispositivos)
        return Response(serializer.data)
    def put(self, request):
        userId= request.GET.get('idDueno', '')
        dispoId= request.GET.get('idDispo', '')
        dispositivos = Dispositivo.objects.get(id=dispoId, propietario_id=userId)
        serializer = DispositivoSerializer(dispositivos, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    def delete(self, request):
        userId= request.GET.get('idDueno', '')
        dispoId= request.GET.get('idDispo', '')
        dispositivos = Dispositivo.objects.get(id=dispoId, propietario_id=userId)
        dispositivos.delete()
        return Response(status=204)

class HorarioList(APIView):
    def get(self, request):
        horarios = Horario.objects.all()
        serializer = HorarioSerializer(horarios, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = HorarioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class HorarioByDispositivo(APIView):
    def get(self, request):
        id=request.GET.get('dispositivoId', '')
        horarios = Horario.objects.filter(Dispo__id=id)
        serializer = HorarioSerializer(horarios, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = HorarioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class HorarioEdit(APIView):
    def get(self, request):
        dispoId = request.GET.get('dispoId', '')
        horarioId = request.GET.get('horarioId', '')
        horarios = Horario.objects.get(id=horarioId, Dispo__id=dispoId)
        serializer = HorarioSerializer(horarios)
        return Response(serializer.data)
    def put(self, request):
        dispoId = request.GET.get('dispoId', '')
        horarioId = request.GET.get('horarioId', '')
        horarios = Horario.objects.get(id=horarioId, Dispo__id=dispoId)
        serializer = HorarioSerializer(horarios, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    def delete(self, request):
        dispoId = request.GET.get('dispoId', '')
        horarioId = request.GET.get('horarioId', '')
        horarios = Horario.objects.get(id=horarioId, Dispo__id=dispoId)
        horarios.delete()
        return Response(status=204)
class PerritoImage(APIView):
    def get(self, request):
        id=request.GET.get('id', '')
        perritos = Perrito.objects.filter(id=id)
        serializer = PerritoSerializer(perritos, many=True)
        return Response(serializer.data)