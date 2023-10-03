class World():
    def __init__(self):
        self.shapes = {}

    def addShape(self, shape):
        self.shapes[shape.getId()] = shape

    def removeShape(self, id):
        del self.shapes[id]

    def printShapes(self):
        for shape in self.shapes.values():
            shape.printCoord()

    def updateShapeCoord(self, id, x, y):
        self.shapes[id].updateCoord(x, y)
    
    def updateShapeColor(self, id, color):
        self.shapes[id].updateColor(color)
    
    
