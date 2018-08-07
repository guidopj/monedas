from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('crearMoneda/<nombreUsuario>/', views.crearMoneda, name="crearMoneda"),
    path('crearUsuario/', views.crearUsuario, name="crearUsuario"),
    path('home', views.autenticarUsuario, name="home"),
]
