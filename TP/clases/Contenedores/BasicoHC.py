
from clases.Contenedores.Contenedor import Contenedor
from clases.Exception.ContenerdorLlenoException import ContenedorLlenoException
from clases.Exception.ExcesoMedidasException import ExcesoMedidasException
from clases.Exception.NoHayContenedoresException import NoHayContenedoresException


class BasicoHC(Contenedor):
    def __init__(self, id):
        super().__init__(id, 235.0, 230.0, 1200.0, 245.0, 260.0, 1210.0)
        self.set_pies(40)
        self.set_max_Peso(32500.0)
        self.set_max_Volumen(67.7)

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