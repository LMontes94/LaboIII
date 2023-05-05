from abc import ABC

class Traccion(ABC):
    def __init__(self,nombre,restaPotencia):
        self.nombre = nombre 
        self.restaPotencia = restaPotencia
    
    def avanzar(self,distancia,hp):
        pass 