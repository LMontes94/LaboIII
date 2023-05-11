from clases.Algoritmo import Algoritmo 
from clases.TareaQueue import TareaQueue
class Prioritario(Algoritmo):
    def __init__(self):
        super().__init__("Prioritario")
        
    def ejecutar_procesos(self,queue_usuario,queue_sistema):
       queue_total = TareaQueue() 
       queue_total = queue_sistema + queue_usuario
       queue_total.sort(key = queue_total.prioridad, reverse = False)
       
       queue_sistema.vaciarQueue()
       queue_usuario.vaciarQueue()
       
       while not queue_total.isEmpty():
           tarea = queue_total.remove()
           self.ejecutar(tarea)
           
       
       
       
       
       