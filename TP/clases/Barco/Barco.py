
from clases.Barco.SistemaPropulsion.SistemaPropulsion import SistemaPropulsion
from clases.Contenedores.Contenedor import Contenedor
from abc import ABC, abstractmethod


class Barco(ABC):

    def __init__(self):
        self.__id = 0
        self.__max_Containers = 0
        self.__max_Peso = 0.0
        self.__conteiner = list()
        self.__sede_Inicial = ''
        self.__sede_Final = ''
        self.__km_Total = 0.0
        self.__es_Especial = False
        self.__peso_Actual = 0.0
        self.__sistema_propulsion: SistemaPropulsion()
        self.__combustible_actual = 0.0
        self.CONSUMO_X_HORA = 6.0

# --------Getters & Setters-----------------
    # getters y setters id

    def get_id(self):
        return self.__id

    def set_id(self, valor):
        self.__id = valor

    id = property(get_id, set_id)

    # getters y setters maxContainers
    def get_max_Containers(self):
        return self.__max_Containers

    def set_max_Containers(self, valor):
        self.__max_Containers = valor

    max_Containers = property(get_max_Containers, set_max_Containers)

    # getters y setters maxPeso

    def get_max_Peso(self):
        return self.__max_Peso

    def set_max_Peso(self, valor):
        self.__max_Containers = valor

    max_Containers = property(get_max_Peso, set_max_Peso)

    # getters y setters conteiner

    def get_conteiner(self):
        return self.__conteiner

    def cargar_conteiner(self, valor):
        self.__conteiner.append(valor)

    conteiner = property(get_conteiner, cargar_conteiner)

    # getters y setters sedeInicial

    def get_sede_Inicial(self):
        return self.__sede_Inicial

    def set_sede_Inicial(self, valor):
        self.__sede_Inicial = valor

    sede_Inicial = property(get_sede_Inicial, set_sede_Inicial)

    # getters y setters sedeFinal
    def get_sede_Final(self):
        return self.__sede_Final

    def set_sede_Final(self, valor):
        self.__sede_Final = valor

    sede_Final = property(get_sede_Final, set_sede_Final)

# getters y setters kmsTotal
    def get_km_Total(self):
        return self.__km_Total

    def set_km_Total(self, valor):
        self.__km_Total = valor

    km_Total = property(get_km_Total, set_km_Total)

# getters y setters es_Especial
    def get_es_Especial(self):
        return self.__es_Especial

    def set_es_Especial(self, valor):
        self.__es_Especial = valor

    es_Especial = property(get_es_Especial, set_es_Especial)

    # getters y setters pesoActual

    def get_peso_Actual(self):
        return self.__peso_Actual

    def set_peso_Actual(self, valor):
        self.__peso_Actual = valor
    peso_Actual = property(get_peso_Actual, set_peso_Actual)

    def get_sistema_propulsion(self):
        return self.__sistema_propulsion

    def set_sistema_propulsion(self, sistema_propulsion):
        self.__sistema_propulsion = sistema_propulsion

    sistema_propulsion = property(
        get_sistema_propulsion, set_sistema_propulsion)

    def get_combustible(self):
        return self.__combustible_actual

    def set_combustible(self, combustible):
        self.__combustible_actual = combustible

    combustible_actual = property(get_combustible, set_combustible)

    def get_consumo_x_hora(self):
        return self.CONSUMO_X_HORA


# --------Getters & Setters-----------------
#  ...........................
# -----------Funciones-----------

    @abstractmethod
    def descargar(self):
        pass

    @abstractmethod
    def obtenerKmRecorridos(self):
        pass

    def marchar(self, tiempo):
        self.sistema_propulsion.activar(tiempo)