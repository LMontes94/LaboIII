from abc import ABC

class Tarea(ABC): 
    def __init__(self,nombre,prioridad,tiempo_ejecucion):
        self.nombre = nombre
        self.prioridad = prioridad
        self.tiempo_ejecucion = tiempo_ejecucion
