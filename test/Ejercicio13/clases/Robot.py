class Robot:
    def __init__(self,nombre,potencia):
        self.nombre = nombre
        self.potencia = potencia 
        self.traccion = None 

    def avanzar(self,distancia):
        pass 

    def configurarSistemaTraccion(self,traccion):
        self.traccion = traccion