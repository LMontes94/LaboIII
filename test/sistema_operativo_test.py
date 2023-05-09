from unittest import TestCase
from src.practica_parcial.clases.SistemaOperativo import SistemaOperativo
from src.practica_parcial.clases.TareaSistema import TareaSistema


class SistemaOperativoTest(TestCase):
   
    def test_agregar_proceso(self):
        tarea = TareaSistema("Nombreee",1,2)
        so = SistemaOperativo()
        so.agregar_proceso(tarea)
        assert len(so.tareas.get('sistema')) > 0