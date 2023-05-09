
from src.practica_parcial.clases.Tarea import Tarea


class TareaUsuario(Tarea):
    def __init__(self,nombre,prioridad,tiempo_ejecucion):
        self.nombre = nombre
        self.prioridad = prioridad
        self.tiempo_ejecucion = tiempo_ejecucion

    def get_nombre(self):
        return self.nombre

    def get_prioridad(self):
        return self.prioridad

    def get_tiempo_ejecucion(self):
        return self.tiempo_ejecucion

    
        