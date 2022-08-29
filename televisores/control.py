class Control:
    def __init__(self) :
        TV=0
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