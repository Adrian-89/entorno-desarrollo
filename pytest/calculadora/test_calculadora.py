# test_calculadora.py

import pytest
from calculadora import sumar, restar, multiplicar, dividir

@pytest.mark.parametrize("a, b, resultado", [
    (1, 2, 3),
    (-1, -1, -2),
    (0, 0, 0),
    (100, 200, 300)
])
def test_sumar(a, b, resultado):
    assert sumar(a, b) == resultado

@pytest.mark.parametrize("a, b, resultado", [
    (2, 1, 1),
    (-1, -1, 0),
    (0, 0, 0),
    (100, 50, 50)
])
def test_restar(a, b, resultado):
    assert restar(a, b) == resultado

@pytest.mark.parametrize("a, b, resultado", [
    (2, 3, 6),
    (-1, -1, 1),
    (0, 1, 0),
    (10, 10, 100)
])
def test_multiplicar(a, b, resultado):
    assert multiplicar(a, b) == resultado

@pytest.mark.parametrize("a, b, resultado", [
    (6, 3, 2),
    (-10, -2, 5),
    (10, 2, 5)
])
def test_dividir(a, b, resultado):
    assert dividir(a, b) == resultado

def test_dividir_por_cero():
    with pytest.raises(ValueError):
        dividir(1, 0)
