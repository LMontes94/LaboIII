from clases.Algoritmo import Algoritmo 
class Alternado(Algoritmo):
    def __init__(self):
        super().__init__("Alternado")
        
    def ejecutar_procesos(self,queue_usuario,queue_sistema):
        
        while not queue_usuario.isEmpty() and not queue_sistema.isEmpty():
            if not queue_sistema.isEmpty():
                tarea = queue_sistema.remove()
                self.ejecutar(tarea)
                
            if not queue_usuario.isEmpty():
                tarea = queue_usuario.remove()
                self.ejecutar(tarea)
                
        print(self.__str__())