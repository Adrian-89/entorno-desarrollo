
def login(nombre_usuario, contraseña, usuario_esperado, contraseña_esperada):
    """
    Compara el nombre de usuario y la contraseña con los valores esperados.

    :param nombre_usuario: Nombre de usuario proporcionado.
    :param contraseña: Contraseña proporcionada.
    :param usuario_esperado: Nombre de usuario esperado.
    :param contraseña_esperada: Contraseña esperada.
    :return: True si el nombre de usuario y la contraseña coinciden con los valores esperados, False en caso contrario.
    """
    return nombre_usuario == usuario_esperado and contraseña == contraseña_esperada

