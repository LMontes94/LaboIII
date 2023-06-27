
from clases.Contenedores.Contenedor import Contenedor
from clases.Exception.CargaNoPermitidaException import CargarNoPermitidaException
from clases.Exception.ContenerdorLlenoException import ContenedorLlenoException
from clases.Exception.ExcesoMedidasException import ExcesoMedidasException
from clases.Exception.NoHayContenedoresException import NoHayContenedoresException
from clases.Mercaderia.Alimento import Alimento
from clases.Mercaderia.Quimico import Quimico


class Ventilado(Contenedor):
    def __init__(self, id):
        super().__init__(id, 235.0, 230.0, 600.0, 245.0, 260.0, 610.0)
        self.set_pies(20)
        self.set_max_Peso(24000.0)
        self.set_max_Volumen(32.6)


    def manejar(self, mercaderia):

        try:
            self.puedeManejar(mercaderia)
            if self.verificarQuimico():              
              self.cargar_mercaderia(mercaderia)
            elif self.verificarAlimento():
               self.cargar_mercaderia(mercaderia)
                
        except (ContenedorLlenoException, ExcesoMedidasException) as e:
          
           print(f"Error {e.get_code()} / {e.get_mensaje}")
           try: 
              self.noHaySiguiente()
              self.siguiente.manejar(mercaderia)
           except NoHayContenedoresException as e:
             print(f"Error {e.get_code()} / {e.get_mensaje}")
    
    def verificarQuimico(self,mercaderia):
        return isinstance(mercaderia,Quimico)
    
    def verificarAlimento(self):
        for contenedor in self.contenedores:
            if contenedor.soloAlimento():
                raise CargarNoPermitidaException("No se permite cargar Alimento junto a otros Alimentos")
        
        return True       