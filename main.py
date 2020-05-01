__author__ = "rgr"

from acciones import tomar_eleccion
from personaje import Personaje

print("Bienvenido a Role Game!")
pj_name = input("Introduce el nombre de tu personaje: ")
pj = Personaje(nombre=pj_name)
print(f"Hola {pj.nombre}")

tomar_eleccion()
