
from src.practica_parcial.clases.TareaSistema import TareaSistema


class SistemaOperativo:
    def __init__(self):
        self.tareas = {
           'sistema': [],
           'usuario': []
        }
        self.algoritmo = "Alternado"

    def agregar_proceso(self,tarea):
        
        if isinstance(tarea, TareaSistema):
            self.tareas['sistema'].append(tarea)
        else:
            self.tareas['usuario'].append(tarea)

    def ejecutar_proceso(self,tarea):
        print(f"Ejecutando proceso {tarea.nombre}")
        i = 0
        while(i < tarea.tiempo_ejecucion):
            i = i + 1
            print(f"Procesando.....{i}")           
        
        print(f"Preceso finalizado.. en {i}s.")

    def eliminar_proceso(self,tarea):
        if isinstance(tarea, TareaSistema):
            return self.tareas['sistema'].remove(tarea)
        
        return self.tareas['usuario'].remove(tarea)

    def alternado(self):
        while self.tareas['sistema'] != 0 and self.tareas['usuario'] != 0:
            if self.tareas['sistema']:
                

