__author__ = "rgr"


def tomar_eleccion():
    eleccion = input(
        """¿Que quieres hacer?
    1. Luchar
    2. Interactuar con personaje
    3. Huir \n""")

    eleccion = int(eleccion)

    if eleccion == 1:
        print("Estás luchando")
    elif eleccion == 2:
        print("Estás interactuando con otro personaje")
    elif eleccion == 3:
        print("¡Has huido!")
    else:
        print("Comando no válido")
        tomar_eleccion()
