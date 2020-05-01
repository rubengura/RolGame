__author__ = "rgr"

from acciones import tomar_eleccion
from personaje import Personaje
personaje=Personaje("Sergio")
print(personaje.nombre)

print("Bienvenido a Role Game!")
pj_name = input("Introduce el nombre de tu personaje: ")
print(f"Hola {pj_name}")

tomar_eleccion()
