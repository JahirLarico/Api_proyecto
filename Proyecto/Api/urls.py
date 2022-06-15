from django.urls import URLPattern, path
from . import views

app_name = "Api"

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('users', views.UserList.as_view(), name='users'),

    path('cities', views.CityList.as_view(), name='cities'),
]