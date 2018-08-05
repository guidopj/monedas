from django.db import models

class Usuario(models.Model):
    nombreUsuario = models.CharField(max_length=30, primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nac = models.DateTimeField()

class Moneda(models.Model):
    nombreMoneda = models.CharField(max_length=30, primary_key=True)
    signo =  models.CharField(max_length=8)
    creadaPor = models.ForeignKey(Usuario, on_delete=models.CASCADE)


class MonedasUsuario(models.Model):
    nombreUsuario = models.ForeignKey(Usuario,on_delete=models.CASCADE)
    nombreMoneda = models.ForeignKey(Moneda,on_delete=models.CASCADE)
    cantMonedas = models.IntegerField()