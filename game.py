__author__ = "rgr"

from acciones import tomar_eleccion
from personaje import Personaje


def start_game():
    print("Bienvenido a Role Game!")

    pj = Personaje()
    print(f"Hola {pj.nombre}")

    tomar_eleccion()