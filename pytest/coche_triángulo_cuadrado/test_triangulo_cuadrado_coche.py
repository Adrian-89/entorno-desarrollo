import pytest

# Pruebas para la clase Coche
def test_acelerar():
    coche = Coche("Toyota", "Corolla", 180)
    coche.acelerar(50)
    assert coche.velocidad_actual == 50

    coche.acelerar(200)
    assert coche.velocidad_actual == 180  # No debe exceder la velocidad máxima

def test_frenar():
    coche = Coche("Toyota", "Corolla", 180)
    coche.acelerar(100)
    coche.frenar(30)
    assert coche.velocidad_actual == 70

    coche.frenar(100)
    assert coche.velocidad_actual == 0  # No debe ser menor que 0

# Pruebas para la clase Triangulo
def test_es_equilatero():
    t = Triangulo(3, 3, 3)
    assert t.es_equilatero()

    t = Triangulo(3, 4, 5)
    assert not t.es_equilatero()

def test_perimetro_triangulo():
    t = Triangulo(3, 4, 5)
    assert t.perimetro() == 12

def test_area_triangulo():
    t = Triangulo(3, 4, 5)
    assert t.area() == 6.0

# Pruebas para la clase Cuadrado
def test_perimetro_cuadrado():
    c = Cuadrado(4)
    assert c.perimetro() == 16

def test_area_cuadrado():
    c = Cuadrado(4)
    assert c.area() == 16
