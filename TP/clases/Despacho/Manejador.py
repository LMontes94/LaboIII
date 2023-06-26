
from abc import ABC, abstractmethod


class Manejador(ABC):

    @abstractmethod
    def manejar(self, mercaderia):
        pass

    def set_siguiente(self, manejador):
        pass
