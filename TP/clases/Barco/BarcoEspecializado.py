from clases.Contenedores.Contenedor import Contenedor
from clases.Barco.Barco import Barco
from clases.Exception.NoHayBarcoException import NoHayBarcoException


class BarcoEspecializado(Barco):

    def __init__(self):
        super().__init__()
        self.es_Especial = True

    def obtenerKmRecorridos(self, inicio, final):
        kmRecorridos = GPS(inicio, final)

        self.km_Total += kmRecorridos
        return kmRecorridos

    def descargar(self):
        contAux = Contenedor()
        listAux = list()
        while self.conteiner:
            contAux = self.conteiner.pop(0)
            listAux.append(contAux)

        self.peso_Actual = 0.0
        return listAux

    def manejar(self, contenedor):

        try:
            if self.puede_cargar_contenedor(contenedor):
                self.cargar_conteiner(contenedor)
            elif self.noHaySiguiente():
                self.set_siguiente().manejar(contenedor)
        except NoHayBarcoException as e:
            print(f"Error {e.get_code()} / {e.get_mensaje()}")

    def puede_cargar_contenedor(self, contenedor):
        if contenedor.get_es_especial():
            return self.verificar_carga_contenedor(contenedor)

        return False
