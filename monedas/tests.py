from django.test import TestCase
from django.conf import settings

# Create your tests here.
import unittest
from monedas.models import Usuario, Moneda,MonedasUsuario
from datetime import date, datetime



class TestModel(TestCase):
    def setUp(self):

        self.usuario1 = Usuario.objects.create(nombreUsuario="usuario1", contrasena="hola", nombre="pepito", apellido="lopez",
                                          fecha_nac=date.today())
        usuario2 = Usuario.objects.create(nombreUsuario="usuario2", contrasena="hola", nombre="pepito", apellido="Gomez",
                                          fecha_nac=date.today())
        moneda = Moneda.objects.create(nombreMoneda="dolar", signo="U$", espesor=1.0, creadaPor=self.usuario1,
                                       fechaCreacion=date.today())

        self.monedasUsuario1 = MonedasUsuario.objects.create(usuario=self.usuario1, moneda=moneda, cantMonedas=100)
        self.monedasUsuario2 = MonedasUsuario.objects.create(usuario=usuario2, moneda=moneda, cantMonedas=39)


    def test_transaccionCorrectaDeMonedas(self):
        user1 = MonedasUsuario.objects.get(usuario="usuario1")
        user2 = MonedasUsuario.objects.get(usuario="usuario2")
        user1.enviarMonedas(user2, 99)
        self.assertEqual(user1.cantMonedas, 1)
        self.assertEqual(user2.cantMonedas, 138)

if __name__ == '__main__':
    unittest.main()