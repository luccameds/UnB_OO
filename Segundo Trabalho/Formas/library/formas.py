class Point ():

    def __init__(self, id, x, y, color):
        self.id = id
        self.x = x
        self.y = y
        self.color = color

    def updateCoord(self, x, y):
        self.x = x
        self.y = y
    
    def updateColor(self, color):
        self.color = color

    def getId(self):
        return self.id
    
    def printCoord(self):
        print("Coordenadas do Ponto: ", self.x, ",", self.y)


class Circulo ():
    def __init__(self, id, x, y, color, raio):
        self.id = id
        self.x = x
        self.y = y
        self.color = color
        self.raio = raio

    def updateCoord(self, x, y):
        self.x = x
        self.y = y
    
    def updateColor(self, color):
        self.color = color

    def getId(self):
        return self.id
    
    def printCoord(self):
        print("Coordenadas do Círculo: ", self.x, ",", self.y)

    def getRaio(self):
        return self.raio

    def setRaio(self, raio):
        self.raio = raio

class Retangulo ():
    def __init__(self, id, x, y, color, largura, altura):
        self.id = id
        self.x = x
        self.y = y
        self.color = color
        self.largura = largura
        self.altura = altura

    def updateCoord(self, x, y):
        self.x = x
        self.y = y
    
    def updateColor(self, color):
        self.color = color

    def getId(self):
        return self.id
    
    def printCoord(self):
        print("Coordenadas do Retângulo: ", self.x, ",", self.y)

    def getLargura(self):
        return self.largura

    def setLargura(self, largura):
        self.largura = largura

    def getAltura(self):
        return self.altura

    def setAltura(self, altura):
        self.altura = altura

class Triangulo ():
    def __init__(self, id, x, y, color, base, altura):
        self.id = id
        self.x = x
        self.y = y
        self.color = color
        self.base = base
        self.altura = altura

    def updateCoord(self, x, y):
        self.x = x
        self.y = y
    
    def updateColor(self, color):
        self.color = color

    def getId(self):
        return self.id
    
    def printCoord(self):
        print("Coordenadas do Triângulo: ", self.x, ",", self.y)

    def getBase(self):
        return self.base

    def setBase(self, base):
        self.base = base

    def getAltura(self):
        return self.altura

    def setAltura(self, altura):
        self.altura = altura