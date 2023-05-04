

from unittest import TestCase

from src.calculadora import Calculadora

class CalculadoraTest(TestCase):

    def test_suma_ok(self):
        calc = Calculadora()
        assert calc.suma(2,1) == 3   