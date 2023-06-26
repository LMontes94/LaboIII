from clases.Mercaderia.Mercaderia import Mercaderia


class Maquinaria(Mercaderia):
    def __init__(self, id, n, p, v, ancho, alto, largo):
        super().__init__(id, n, p, v, ancho, alto, largo)
