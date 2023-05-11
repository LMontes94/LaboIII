from clases.Tarea import Tarea 
class TareaSistema(Tarea):
    def __init__(self,nombre,prioridad,tiempo_ejecucion):
        super().__init__(nombre,prioridad,tiempo_ejecucion)
        self.tipo = "Sistema"