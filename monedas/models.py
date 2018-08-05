from django.db import models
from datetime import datetime

class Usuario(models.Model):
    nombreUsuario = models.CharField(max_length=30, primary_key=True)
    contrasena = models.CharField(max_length=100, default='')
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nac = models.DateField(
                blank=False, null=False)

class Moneda(models.Model):
    nombreMoneda = models.CharField(max_length=30, primary_key=True)
    signo = models.CharField(max_length=8)
    peso = models.IntegerField(default=0)
    espesor = models.FloatField(default=0.0)
    creadaPor = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fechaCreacion = models.DateTimeField(default=datetime.now)



class MonedasUsuario(models.Model):
    nombreUsuario = models.ForeignKey(Usuario,on_delete=models.CASCADE)
    nombreMoneda = models.ForeignKey(Moneda,on_delete=models.CASCADE)
    cantMonedas = models.IntegerField(default=0)