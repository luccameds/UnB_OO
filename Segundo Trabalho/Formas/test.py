from library.formas import Point # Importa a classe Point do módulo formas
from library.formas import Circulo # Importa a classe Circulo do módulo formas
from library.formas import Retangulo # Importa a classe Retangulo do módulo formas
from library.formas import Triangulo # Impota a classe Triangulo do módulo formas
from library.world import World # Importa a classe World do módulo world

# Teste de funções
print("\nTeste de funções")

#Criando um Ponto
print("\nCriando um objeto Ponto...")
forma = Point(1, 10, 20, "Azul")

print("Coordenadas: ", forma.x, ",", forma.y)
print("Cor: ", forma.color)

print("\nAtualizando coordenadas...")
forma.updateCoord(100, 200)
print("Coordenadas: ", forma.x, ",", forma.y)

print("\nAtualizando cor...")
forma.updateColor("Vermelho")
print("Cor: ", forma.color)
print("Id: ", forma.getId())

print("\nImprimindo coordenadas...")
forma.printCoord()

print("----------------------------------")


#Criando um Círculo
print("Criando um objeto Circulo...")
forma = Circulo(1, 10, 20, "Azul", 5)
print("Coordenadas: ", forma.x, ",", forma.y)
print("Cor: ", forma.color)
print("Raio: ", forma.getRaio())

print("\nAtualizando coordenadas...")
forma.updateCoord(100, 200)
print("Coordenadas: ", forma.x, ",", forma.y)

print("Atualizando cor...")
forma.updateColor("Vermelho")
print("Cor: ", forma.color)
print("Id: ", forma.getId())

print("Atualizando raio...")
forma.setRaio(10)
print("Raio: ", forma.getRaio())

print("\nImprimindo coordenadas...")
forma.printCoord()

print("----------------------------------")


# Criando um Retângulo
print("Criando um objeto Retangulo...")
forma = Retangulo(1, 10, 20, "Azul", 10, 20)
print("Coordenadas: ", forma.x, ",", forma.y)
print("Cor: ", forma.color)
print("Largura: ", forma.largura)
print("Altura: ", forma.altura)

print("\nAtualizando coordenadas...")
forma.updateCoord(100, 200)
print("Coordenadas: ", forma.x, ",", forma.y)

print("Atualizando cor...")
forma.updateColor("Vermelho")
print("Cor: ", forma.color)
print("Id: ", forma.getId())

print("\nAtualizando largura...")
forma.setLargura(20)
print("Largura: ", forma.getLargura())

print("\nImprimindo coordenadas...")
forma.printCoord()

print("----------------------------------")


# Criando um Triângulo
print("Criando um objeto Triangulo...")
forma = Triangulo(1, 10, 20, "Azul", 10, 20)
print("Coordenadas: ", forma.x, ",", forma.y)
print("Cor: ", forma.color)
print("Largura: ", forma.base)
print("Altura: ", forma.altura)

print("\nAtualizando coordenadas...")
forma.updateCoord(100, 200)
print("Coordenadas: ", forma.x, ",", forma.y)

print("Atualizando cor...")
forma.updateColor("Vermelho")
print("Cor: ", forma.color)
print("Id: ", forma.getId())

print("\nAtualizando largura...")
forma.setBase(20)
print("Largura: ", forma.getBase())

print("\nImprimindo coordenadas...")
forma.printCoord()

print("----------------------------------")

# Criando Mundo
print("Criando um objeto World...")

world = World()

print("\nAdicionando formas...")
world.addShape(Point(1, 10, 20, "Azul"))
world.addShape(Circulo(2, 20, 30, "Vermelho", 5))
world.addShape(Retangulo(3, 30, 40, "Verde", 10, 20))
world.addShape(Triangulo(4, 40, 50, "Amarelo", 10, 20))

print("\nImprimindo formas...")
world.printShapes()

print("\nAtualizando coordenadas...")
world.updateShapeCoord(1, 100, 200)
world.updateShapeCoord(2, 200, 300)
world.updateShapeCoord(3, 300, 400)
world.updateShapeCoord(4, 400, 500)

print("\nImprimindo formas...")
world.printShapes()

print("\nAtualizando cores...")
world.updateShapeColor(1, "Vermelho")
world.updateShapeColor(2, "Verde")
world.updateShapeColor(3, "Amarelo")
world.updateShapeColor(4, "Azul")

print("\nImprimindo formas...")
world.printShapes()

print("\nRemovendo formas...")
world.removeShape(1)
world.removeShape(2)
world.removeShape(3)
world.removeShape(4)

print("\nImprimindo formas...")
world.printShapes()

print("----------------------------------")