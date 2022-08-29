




class televisores:
    def __init__(self) -> None:
        pass

    class Marca:
        def __init__ (self, nombre,):
            self.nombre = nombre
        def getNombre (self):
            return self.nombre
        def setNombre (self, nombre):
            self.nombre = nombre

    class TV:
        numTV = 0
        def __init__(self,marca,estado) :
            self.marca = Marca(self)
            self.canal = 1
            self.precio = 500
            self.estado = estado
            self.volumen = 1
            self.control = Control()
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


    class Control:
        def __init__(self) :
            self.tv = TV

        def volumenUp(self):
            return self.tv.volumenUp()
        def volumenDown(self):
            return self.tv.volumenDown()
        def canalUp(self):
            return self.tv.canalUp()
        def canalDown(self):
            return self.tv.canalDown()
        def turnOff(self):
            return self.tv.turnOff()
        def turnOn(self):
            return self.tv.turnOn()
        def setCanal (self,canal):
            return self.tv.setCanal(canal)
        def enlazar (self,tv):
            self.tv = tv
            tv.setControl(tv)
        def getTv(self):
            return self.tv
        def setTv(self,tv):
            self.tv = tv

    
    

