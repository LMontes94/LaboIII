
from operator import truediv
from unittest import TestCase
from src.ejercicio.clases.Oruga import Oruga
from src.ejercicio.clases.SensorTemperatura import SensorTemperatura

class OrugaTest(TestCase):
    def test_oruga_avanza(self):
        oruga = Oruga()
        avanzo = oruga.avanzar(250,10)
        assert avanzo
    
    def test_oruga_agregar_sensor_not_empty(self):
        oruga = Oruga()
        sensor = SensorTemperatura()
        oruga.agregarSensor(sensor)
        assert oruga.sensores != None


    def test_oruga_agregar_sensor_empty(self):
        oruga = Oruga()
        sensor = SensorTemperatura()
        assert oruga.sensores == []

    def test_oruga_cambiar_oruga(self):
        oruga = Oruga()
        oruga.avanzar(250,10)
        oruga.avanzar(100,10)
        oruga.avanzar(50,10)
        oruga.cambiarOruga()
        assert oruga.rodado == 400

    def test_oruga_is_not_new(self):
        oruga = Oruga()
        oruga.avanzar(250,10)
        oruga.avanzar(100,10)
        oruga.avanzar(50,10)
        assert oruga.rodado != 400