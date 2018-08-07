from django.test import TestCase
from django.conf import settings
settings.configure()
# Create your tests here.
import unittest
from monedas.models import Usuario, Moneda,MonedasUsuario
from datetime import date, datetime



class TestModel(TestCase):
    def setUp(self):

        usuario1 = Usuario.objects.create(userName="usuario1", contrasena="hola", nombre="pepito", apellido="lopez",
                                          fecha_nac=datetime.date(2002, 3, 11))
        usuario2 = Usuario.objects.create(userName="usuario2", contrasena="hola", nombre="pepito", apellido="Gomez",
                                          fecha_nac=datetime.date(2005, 3, 11))
        moneda = Moneda.objects.create(nombreMoneda="dolar", signo="U$", espesor=1.0, creadaPor=usuario1,
                                       fechaCreacion=date.today())

        self.monedasUsuario1 = MonedasUsuario(nombreUsuario=usuario1, nombreMoneda=moneda, cantMonedas=100)
        self.monedasUsuario2 = MonedasUsuario(nombreUsuario=usuario2, nombreMoneda=moneda, cantMonedas=39)


    def test_transaccionCorrectaDeMonedas(self):
        user1 = self.monedasUsuario1.objects.get(userName="usuario1")
        user2 = self.monedasUsuario2.objects.get(userName="usuario2")
        user1.enviarMonedas(user2, 99)
        self.assertEqual(user1.cantMonedas, 1)
        self.assertEqual(user2.cantMonedas, 138)

if __name__ == '__main__':
    unittest.main()