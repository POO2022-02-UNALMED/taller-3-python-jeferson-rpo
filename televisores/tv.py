from asyncio.windows_events import NULL


class TV:
    numTV = 0
   
    def __init__(self,marca,estado) :
        control = 0
        self.marca = marca
        self.canal = 1
        self.precio = 500
        self.estado = estado
        self.volumen = 1
        self.control = control
        self.numTV += 1
    
    def turnOn (self):
        self.estado = True
        
    
    def turnOff (self):
        if self.estado == True:
            self.estado = False

    def canalUp(self):
        if self.canal<120 and self.estado==True:
            self.canal =self.canal + 1

    def canalDown(self):
            if self.canal>1 and self.estado==True:
                self.canal =self.canal - 1

    def volumenUp(self):
        if self.volumen < 7 and self.estado==True:
            self.volumen =self.volumen + 1

    def volumenDown(self):
        if self.volumen>1 and self.estado==True:
            self.volumen =self.volumen - 1   
        
    def getEstado (self):
        return self.estado

    def getMarca (self):
        return self.marca

    def setMarca (self, marca):
        self.marca = marca

    def getControl (self):
        return self.control

    def setControl (self, control):
        self.control = control
    
    def getPrecio (self):
        return self.precio

    def setPrecio (self, precio):
        self.precio = precio

    def getVolumen(self):
        return self.volumen

    def setVolumen(self, volumen):
        self.volumen= volumen

    def getCanal (self):
        return self.canal

    def setCanal (self, canal):
        if canal < 121 and self.estado == True:
            self.canal = canal