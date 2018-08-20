from django.test import TestCase

# Create your tests here.
import unittest
from monedas.models import Usuario, Moneda,MonedasUsuario
from datetime import date, datetime
from django.core.exceptions import ValidationError



class TestModel(TestCase):
    def setUp(self):

        self.usuario1 = Usuario.objects.create(nombreUsuario="usuario1", contrasena="hola", nombre="pepito", apellido="lopez",
                                          fecha_nac=date.today())
        usuario2 = Usuario.objects.create(nombreUsuario="usuario2", contrasena="hola", nombre="pepito", apellido="Gomez",
                                          fecha_nac=date.today())
        self.moneda = Moneda.objects.create(nombreMoneda="dolar", signo="U$", espesor=1.0, creadaPor=self.usuario1,
                                       fechaCreacion=date.today())
        self.monedasUsuario1 = MonedasUsuario.objects.create(usuario=self.usuario1, moneda=self.moneda, cantMonedas=100)
        self.monedasUsuario2 = MonedasUsuario.objects.create(usuario=usuario2, moneda=self.moneda, cantMonedas=39)



    def test_transaccionCorrectaDeMonedasAUsuarioExistente(self):
        user1 = MonedasUsuario.objects.get(usuario="usuario1")
        user2 = MonedasUsuario.objects.get(usuario="usuario2")
        user1.enviarMonedasExistente(99, user2)
        self.assertEqual(user1.cantMonedas, 1)
        self.assertEqual(user2.cantMonedas, 138)

    def test_transaccionIncorrectaDeMonedasAUsuarioExistente(self):
        user1 = MonedasUsuario.objects.get(usuario="usuario1")
        user2 = MonedasUsuario.objects.get(usuario="usuario2")
        with self.assertRaises(ValidationError) as context:
            user1.enviarMonedasExistente(101, user2)


    def test_transaccionCorrectaDeMonedasAUsuarioNOExistente(self):
        user1 = MonedasUsuario.objects.get(usuario="usuario1")
        user3 = user1.enviarMonedasANuevo(99, Usuario("usuario3"), self.moneda)
        self.assertEqual(user1.cantMonedas, 1)
        self.assertEqual(user3.cantMonedas, 99)

    def test_transaccionIncorrectaDeMonedasAUsuarioNOExistente(self):
        user1 = MonedasUsuario.objects.get(usuario="usuario1")
        with self.assertRaises(ValidationError) as context:
            user1.enviarMonedasANuevo(101, Usuario("usuario3"), self.moneda)

if __name__ == '__main__':
    unittest.main()