# Definición de las Clases

class Coche:
    def __init__(self, marca, modelo, velocidad_maxima):
        self.marca = marca
        self.modelo = modelo
        self.velocidad_maxima = velocidad_maxima
        self.velocidad_actual = 0

    def acelerar(self, incremento):
        self.velocidad_actual += incremento
        if self.velocidad_actual > self.velocidad_maxima:
            self.velocidad_actual = self.velocidad_maxima

    def frenar(self, decremento):
        self.velocidad_actual -= decremento
        if self.velocidad_actual < 0:
            self.velocidad_actual = 0

class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def es_equilatero(self):
        return self.lado1 == self.lado2 == self.lado3

    def perimetro(self):
        return self.lado1 + self.lado2 + self.lado3

    def area(self):
        s = self.perimetro() / 2
        return (s * (s - self.lado1) * (s - self.lado2) * (s - self.lado3)) ** 0.5

class Cuadrado:
    def __init__(self, lado):
        self.lado = lado

    def perimetro(self):
        return 4 * self.lado

    def area(self):
        return self.lado ** 2




