from src.ejercicio.clases.Traccion import Traccion
class Oruga(Traccion):
    def __init__(self):
        super().__init__("Oruga", 3)
        self.rodado = 400
        self.sensores = []

    def agregarSensor(self,sensor):
        self.sensores.append(sensor)

    def avanzar(self,distancia,hp):
        if (distancia * hp / hp - self.restaPotencia) <= self.rodado:
            self.rodado -= distancia
            for sensor in self.sensores:
                temperatura = sensor.medirTemperatura()
                print(f"Temperatura medida: {temperatura}")
            return True
        else:
            print("Hay que cambiar la oruga!!!")
            return False 

    def cambiarOruga(self):
        self.rodado = 400 
        print("Se cambio la oruga!!!")

