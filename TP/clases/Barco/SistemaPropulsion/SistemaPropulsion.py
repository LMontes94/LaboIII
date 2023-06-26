
from abc import ABC, abstractmethod


class SistemaPropulsion(ABC):
    @abstractmethod
    def gastoCombustible(self, barco):
        pass

    def activar(self, barco):
        pass

    def getNombre():
        pass
