
from clases.Contenedores.Contenedor import Contenedor
from clases.Exception.ContenerdorLlenoException import ContenedorLlenoException
from clases.Exception.ExcesoMedidasException import ExcesoMedidasException
from clases.Exception.NoHayContenedoresException import NoHayContenedoresException


class FlatRack(Contenedor):
    def __init__(self, id):
        super().__init__(id, None, 230.0, 600.0, None, 230.0, 610.0)
        self.set_max_Peso(45000.0)
        self.set_max_Volumen(33.0)
        self.set_es_especial(True)
    
    def validarCargaMercaderia(self, mercaderia):
        if self.get_hay_Espacio() :
                raise ContenedorLlenoException("El contenedor esta lleno!!")
        elif self.get_interior().alto < mercaderia.medida.alto or self.get_interior().largo < mercaderia.medida.largo:
                raise ExcesoMedidasException(f"Las medidas de la {mercaderia.nombre} exceden el limite!!")
        return True
    
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