
from clases.Contenedores.Contenedor import Contenedor
from clases.Exception.ContenerdorLlenoException import ContenedorLlenoException
from clases.Exception.ExcesoMedidasException import ExcesoMedidasException
from clases.Exception.NoHayContenedoresException import NoHayContenedoresException


class OpenTop(Contenedor):
    def __init__(self, id, int_ancho, int_largo, ext_ancho, ext_largo):
        super().__init__(id, int_ancho, None, int_largo, ext_ancho, None, ext_largo)
        self.poner_cobertor = False

    def manejar(self, mercaderia):

        try:
            self.puedeManejar(mercaderia)              
            self.cargar_mercaderia(mercaderia)
        except (ContenedorLlenoException, ExcesoMedidasException) as e:
          
           print(f"Error {e.get_code()} / {e.get_mensaje}")
           try: 
              self.noHaySiguiente()
              self.siguiente.manejar(mercaderia)
           except NoHayContenedoresException as e:
             print(f"Error {e.get_code()} / {e.get_mensaje}")

        
    
    def puedeManejar(self, mercaderia):
       return self.validarCargaMercaderia(mercaderia)
    