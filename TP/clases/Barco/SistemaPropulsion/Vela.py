from SistemaPropulsion.SistemaPropulsion import SistemaPropulsion


class Vela(SistemaPropulsion):
    def __init__(self):
        self.nombre = "Vela"

    def getNombre(self):
        return self.nombre

    def gastoCombustible(self, barco):
        return 0 * barco.get_viaje().get_horas()

    def activar(self, barco):
        self.avanzar(barco.get_viaje().get_horas())

    def avanzar(self, tiempo):
        print(f"El barco avanza por {tiempo} tiempo")
