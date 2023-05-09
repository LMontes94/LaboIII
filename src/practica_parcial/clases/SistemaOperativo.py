
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
        while self.tareas['sistema'] != 0 or self.tareas['usuario'] != 0:
            if self.tareas['sistema']: 
                tarea_sistema = self.tareas['sistema'].pop(0)
                self.ejecutar_proceso(tarea_sistema)
            else:
                tarea_usuario = self.tareas['usuario'].pop(0)
                self.ejecutar_proceso(tarea_usuario)               
    
    def secuencial(self):
        for tarea in self.tareas['sistema']: 
            self.ejecutar_proceso(tarea)
            self.tareas['sistema'].pop()
        for tarea in self.tareas['usuario']:
            self.ejecutar_proceso(tarea)
            self.tareas['usuario'].pop()

    def prioritario(self):
        todas_tareas = self.tareas['sistema'] + self.tareas['usuario']
        todas_tareas.sort(key=self.prioritario, reverse = False)
        self.vaciar_procesos(self.tareas['sistema'])
        self.vaciar_procesos(self.tareas['usuario'])

        for tarea in todas_tareas:
           self.ejecutar_proceso(tarea)
           todas_tareas.pop()

    def vaciar_procesos(self,tareas):
        while tareas != 0:
            tareas.pop()

    def seleccionarAlgortimo(self,algoritmo):
        self.algoritmo = algoritmo
