from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import filters
from rest_framework import generics
from .serializers import *


class IndexView(APIView):
    def get(self,request):
        context = {
            'mensaje' :'servidor activo'
        }
        return Response(context)

class UserList(APIView):
    def get(self, request):
        users = Usuario.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

class PerritoList(APIView):
    def get(self, request):
        perritos = Perrito.objects.all()
        serializer = PerritoSerializer(perritos, many=True)
        return Response(serializer.data)
class DispositivoList(APIView):
    def get(self, request):
        dispositivos = Dispositivo.objects.all()
        serializer = DispositivoSerializer(dispositivos, many=True)
        return Response(serializer.data)
class UserDetail(APIView):
    def get(self, request, pk):
        user = Usuario.objects.get(pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    def get_queryset(self):
        return Usuario.objects.all()