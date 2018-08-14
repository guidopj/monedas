from django.db import models
from datetime import datetime
from django.core.exceptions import ValidationError

class Usuario(models.Model):
    nombreUsuario = models.CharField(max_length=30, primary_key=True)
    contrasena = models.CharField(max_length=100, default='')
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nac = models.DateField(
                blank=False, null=False)
    last_login = models.DateField(
                blank=False, null=False, default=datetime.now())

    def __str__(u):
        return u.nombreUsuario

class Moneda(models.Model):
    nombreMoneda = models.CharField(max_length=30, primary_key=True)
    signo = models.CharField(max_length=8)
    peso = models.IntegerField(default=0)
    espesor = models.FloatField(default=0.0)
    creadaPor = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fechaCreacion = models.DateField(default=datetime.now)

    def __str__(m):
        return m.nombreMoneda



class MonedasUsuario(models.Model):
    usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE)
    moneda = models.ForeignKey(Moneda,on_delete=models.CASCADE)
    cantMonedas = models.IntegerField(default=0)

    def poseeSufMonedas(self, cantPedidas):
        return self.cantMonedas >= cantPedidas

    def enviarMonedas(self, userRecibe, cantPedidas):
        if self.poseeSufMonedas(cantPedidas):
            userRecibe.cantMonedas = userRecibe.cantMonedas + cantPedidas
            self.cantMonedas = self.cantMonedas - cantPedidas
        else:
            raise ValidationError("No tenes suficientes monedas")

class Historial(models.Model):
    accion = models.CharField(max_length=100, null=True)
    usuarioCreador = models.CharField(max_length=100, null=True)
    usuarioEnvia = models.CharField(max_length=100, null=True)
    usuarioRecibe = models.CharField(max_length=100, null=True)
    moneda = models.CharField(max_length=100, null=True)
    cantMonedas = models.IntegerField(default=0)
    fechaTransaccion = models.DateTimeField(default=datetime.now)