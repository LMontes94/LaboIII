from src.ejercicio.clases.Traccion import Traccion
class Rueda(Traccion):
    def __init__(self):
        super().__init__("Rueda de Caucho",1)
        self.rodado = 100 
    
    def avanzar(self,distancia):
        if distancia <= self.rodado:
            self.rodado -= distancia
            return True
        else:
            print("Hay que cambiar la rueda!!!")
            return False 

    def cambiarRueda(self):
        self.rodado = 100
        print("Se cambio la rueda!!!")

    
    