
from abc import ABC, abstractmethod

from clases.Exception.NoHayContenedoresException import NoHayContenedoresException


class Manejador(ABC):

    def __init__(self):
        self.siguiente = None

    def setSiguiente(self, manejador):
        self.siguiente = manejador

    @abstractmethod
    def manejar(self, mercaderia):
        pass

    def noHaySiguiente(self):
         if self.siguiente is None:            
           raise NoHayContenedoresException("Ningún contenedor disponible!!")
       
