from clases.Despacho.Manejador import Manejador
from clases.Exception.NoHayContenedoresException import NoHayContenedoresException


class DespachoMercaderia(Manejador):
    def manejar(self, mercaderia):        
       
       try:
          self.siguiente.manejar(mercaderia) 
       except NoHayContenedoresException as e:
          print(f"Error {e.get_code()} / {e.get_mensaje}") 
          

