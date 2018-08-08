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

class Moneda(models.Model):
    nombreMoneda = models.CharField(max_length=30, primary_key=True)
    signo = models.CharField(max_length=8)
    peso = models.IntegerField(default=0)
    espesor = models.FloatField(default=0.0)
    creadaPor = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fechaCreacion = models.DateField(default=datetime.now)



class MonedasUsuario(models.Model):
    nombreUsuario = models.ForeignKey(Usuario,on_delete=models.CASCADE)
    nombreMoneda = models.ForeignKey(Moneda,on_delete=models.CASCADE)
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
    usuarioEnvia = models.ForeignKey(Usuario,on_delete=models.CASCADE,related_name='usuarioEnvia')
    usuarioRecibe = models.ForeignKey(Usuario,on_delete=models.CASCADE,related_name='usuarioRecibe')
    moneda = models.ForeignKey(Moneda,on_delete=models.CASCADE)
    fechaTransaccion = models.DateTimeField(default=datetime.now)