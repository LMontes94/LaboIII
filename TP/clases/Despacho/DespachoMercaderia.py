from clases.Despacho.Manejador import Manejador


class DespachoMercaderia(Manejador):
    def __init__(self):
        self.siguiente = Manejador()

    def manejar(self, mercaderia):
        return 0

    def setSiguiente(self, manejador):
        self.siguiente = manejador
