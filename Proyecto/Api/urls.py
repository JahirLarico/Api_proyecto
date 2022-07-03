from django.urls import path
from . import views

app_name = "Api"
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('login', TokenObtainPairView.as_view(), name='token_obtain_pair'),

    #Users
    path('users', views.UserList.as_view(), name='users'),
    path('userDetail' , views.UserDetail.as_view(), name='userDetail'),

    path('userJampi', views.UserJampi.as_view(), name='userJampi'),
    #Perritos
    path('perritos', views.PerritoList.as_view(), name='perritos'),
    path('user/perros', views.PerritosByUser.as_view(), name='perros'),
    path('user/perros/edit', views.PerritoEdit.as_view(), name='perrito-edit'),
    #Dispositivos
    path('dispositivos',views.DispositivoList.as_view(), name='dispositivos'),
    path('user/dispositivos', views.DispositivoByUser.as_view(), name='dispositivos'),
    path('user/dispositivos/edit', views.DispositivoEdit.as_view(), name='dispositivo-edit'),
    #Horarios
    path('horarios',views.HorarioList.as_view(), name='horarios'),
    path('dispositivo/horarios',views.HorarioByDispositivo.as_view(), name='horarios'),
    path('dispositivo/horarios/edit',views.HorarioEdit.as_view(), name='horario-edit'),
    #General
    path('users', views.UserList.as_view(), name='users'),
    path('perritos', views.PerritoList.as_view(), name='perritos'),
    path('dispositivos',views.DispositivoList.as_view(), name='dispositivos'),
    path('horarios',views.HorarioList.as_view(), name='horarios'),
]