from SistemaPropulsion.SistemaPropulsion import SistemaPropulsion
from clases.Exception.CombustibleInsuficienteException import CombustibleInsuficienteException


class Motor(SistemaPropulsion):
    def __init__(self):
        self.nombre = "Motor"

    def getNombre(self):
        return self.nombre

    def gastoCombustible(self, barco):
        return barco.get_consumo_x_hora() * barco.get_viaje().get_horas()

    def activar(self, barco):
        if (barco.get_combustible() < self.gastoCombustible(barco)):
            raise CombustibleInsuficienteException(
                "No alcanza el combustible para terminar el viaje!!")
        self.avanzar(barco.get_viaje().get_horas())

    def avanzar(self, tiempo):
        print(f"El barco avanza.. tiempo estimado del viaje: {tiempo}")
