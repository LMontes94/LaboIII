
class TareaQueue:
    def __init__(self):
        self.queue = []
        
    def add(self,tarea):
        self.queue.append(tarea)
        
    def remove(self):
        return self.queue.pop(0)
    
    def tamanio(self):
        return len(self.queue)
    
    def isEmpty(self):
        return self.tamanio() == 0
    
    def vaciarQueue(self):
        while not self.isEmpty():
              self.remove()