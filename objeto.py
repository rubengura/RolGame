__author__ = "rgr"


class Objeto:
    def __init__(self, nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion


class Equipo(Objeto):
    def __init__(self, nombre, descripcion, peso, defensa):
        Objeto.__init__(self, nombre=nombre, descripcion=descripcion)
        self.peso = peso
        self.defensa = defensa
