from django.urls import URLPattern, path
from . import views

app_name = "Api"

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('users', views.UserList.as_view(), name='users'),
    path('users/<int:pk>', views.UserDetail.as_view(), name='user-detail'),
    path('perritos', views.PerritoList.as_view(), name='perritos'),
    path('dispositivos',views.DispositivoList.as_view(), name='dispositivos'),
]