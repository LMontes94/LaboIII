from abc import ABC, abstractmethod
class Algoritmo(ABC):
    def __init__(self,nombre):
        self.nombre = nombre 
        
    @abstractmethod
    def ejecutar_procesos(self,tarea_u,tarea_s):
        pass
    
    def ejecutar(self,tarea):
        print(f"Ejecutando proceso {tarea.nombre}")
        print("------------------------------------")
        i = 0
        while(i < tarea.tiempo_ejecucion):
            i = i + 1
            print(f"Procesando.....{i}")           
        
        print(f"Proceso finalizado.. en {i}s.")
        print("------------------------------------")
        
    def __str__(self):
        return (f"Algoritmo {self.nombre} finalizado")