# test_autenticacion.py

import pytest
from autenticacion import login

@pytest.mark.parametrize("nombre_usuario, contraseña, usuario_esperado, contraseña_esperada, resultado_esperado", [
    ("user1", "password1", "user1", "password1", True),
    ("user2", "password2", "user2", "password2", True),
    ("user3", "wrong_password", "user3", "password3", False),
    ("wrong_user", "password4", "user4", "password4", False),
    ("user5", "password5", "user5", "wrong_password", False),
])
def test_login(nombre_usuario, contraseña, usuario_esperado, contraseña_esperada, resultado_esperado):
    assert login(nombre_usuario, contraseña, usuario_esperado, contraseña_esperada) == resultado_esperado
