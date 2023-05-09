
from src.practica_parcial.clases.Tarea import Tarea


class TareaSistema(Tarea):
    def __init__(self,nombre,prioridad,tiempo_ejecucion):
        self.nombre = nombre
        self.prioridad = prioridad
        self.tiempo_ejecucion = tiempo_ejecucion

    