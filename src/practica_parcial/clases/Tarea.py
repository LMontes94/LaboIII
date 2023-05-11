
from abc import ABC

class Tarea(ABC): 
    def __init__(self,nombre,prioridad,tiempo_ejecucion):
        self.__nombre = nombre
        self.__prioridad = prioridad
        self.__tiempo_ejecucion = tiempo_ejecucion

    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self,nombre):
        self.__nombre = nombre 
        
    def get_prioridad(self):
        return self.__prioridad
    
    def set_prioridad(self,prioridad):
        self.__prioridad = prioridad
        
    def get_tiempo_ejecucion(self):
        return self.__tiempo_ejecucion
    
    def set_tiempo_ejecucion(self,time):
        self.__tiempo_ejecucion = time 
        
    nombre = property(get_nombre,set_nombre)
    prioridad = property(get_prioridad,set_prioridad)
    tiempo_ejecucion = property(get_tiempo_ejecucion,set_tiempo_ejecucion)
    
    
    
    