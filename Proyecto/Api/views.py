from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
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

class CityList(APIView):
    def get(self, request):
        cities = City.objects.all()
        serializer = CitySerializer(cities, many=True)
        return Response(serializer.data)