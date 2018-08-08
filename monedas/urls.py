from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('crearMoneda/<slug:user>/', views.crearMoneda, name="crearMoneda"),
    #path('enviarMoneda', views.enviarMoneda, name="enviarMonedas"),
    path('crearUsuario/', views.crearUsuario, name="crearUsuario"),
    path('autenticar', views.autenticarUsuario, name="autenticar")
]
