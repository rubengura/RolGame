__author__ = "rgr"


def tomar_eleccion():
    eleccion = input(
        """¿Que quieres hacer?
    1. Luchar
    2. Interactuar con personaje
    3. Huir \n""")

    # Pasamos el contenido de eleccion a integer ya que se recoge como string
    eleccion = int(eleccion)

    if eleccion == 1:
        print("Estás luchando")
    elif eleccion == 2:
        print("Estás interactuando con otro personaje")
    elif eleccion == 3:
        print("¡Has huido!")
    # Si la opción elegida no es ninguna de las anteriores, volvemos a pedir al usuario que
    # tome una elección.
    else:
        print("Comando no válido")
        tomar_eleccion()
