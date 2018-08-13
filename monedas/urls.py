from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('crearMoneda/<user>/', views.crearMoneda, name="crearMoneda"),
    path('comprarMonedas/<user>/', views.comprarMonedas, name="comprarMonedas"),
    path('enviarMonedas/<user>/', views.enviarMonedas, name="enviarMonedas"),
    path('crearUsuario/', views.crearUsuario, name="crearUsuario"),
    path('autenticar', views.autenticarUsuario, name="autenticar"),
    path('home/<user>/', views.home, name="autenticar"),
    path('balance/<user>/', views.balance, name="balance")
]
