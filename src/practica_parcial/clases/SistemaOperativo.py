from clases.Alternado import Alternado 
from clases.TareaQueue import TareaQueue

class SistemaOperativo:
    def __init__(self):
        self.algoritmo = Alternado()
        self.tareas_sistema = TareaQueue()
        self.tareas_usuario = TareaQueue()
        
    
    def seleccionar_algoritmo(self,algoritmo):
        self.algoritmo = algoritmo
        
    def get_algoritmo(self):
        return self.algoritmo
    
    
        
        