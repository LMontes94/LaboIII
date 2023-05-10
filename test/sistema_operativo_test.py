from unittest import TestCase
from src.practica_parcial.clases.SistemaOperativo import SistemaOperativo
from src.practica_parcial.clases.TareaSistema import TareaSistema
from src.practica_parcial.clases.TareaUsuario import TareaUsuario

class SistemaOperativoTest(TestCase):
   
    def test_agregar_proceso(self):
        tarea = TareaSistema("Nombreee",1,2)
        so = SistemaOperativo()
        so.agregar_proceso(tarea)
        assert len(so.tareas.get('sistema')) > 0

    def test_eliminar_proceso(self):
        tarea = TareaSistema("Nombreee",1,2)
        so = SistemaOperativo()
        so.agregar_proceso(tarea)
        so.agregar_proceso(tarea)
        so.eliminar_proceso(tarea)
        so.eliminar_proceso(tarea)
        assert len(so.tareas.get('sistema')) == 0

    def test_algoritmo_alternado(self):
         so = SistemaOperativo()
         tarea = TareaSistema("Nombreee",1,2)
         so.agregar_proceso(tarea)
         tarea = TareaSistema("Nombreee1",1,2)
         so.agregar_proceso(tarea)
         tarea = TareaSistema("Nombreee1",0,3)
         so.agregar_proceso(tarea)
         tarea_usu = TareaUsuario("name",8,5)
         so.agregar_proceso(tarea_usu)
         tarea_usu = TareaUsuario("name1",7,9)
         so.agregar_proceso(tarea_usu)
         tarea_usu = TareaUsuario("name2",4,5)
         so.agregar_proceso(tarea_usu)
         tarea_usu = TareaUsuario("name3",6,4)
         so.agregar_proceso(tarea_usu)

         so.alternado()
         assert len(so.tareas.get('sistema')) == 0 and len(so.tareas.get('usuario')) == 0