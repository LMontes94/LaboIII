class Robot:
    def __init__(self):
        self.nombre = "KT-2020"
        self.potencia = 10 
        self.traccion = None   

    def configurarSistemaTraccion(self,traccion):
        self.traccion = traccion