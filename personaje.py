class Personaje:
    def __init__(self, nombre):
        self.nombre = nombre
        self.fuerza = 20
        self.magia = 10
        self.hp = self.fuerza * 5
        self.pm = self.magia * 5
        self.habilidad = 15
        self.carisma = 15
        self.nivel = 1
        self.capacidad_peso = self.fuerza * 3

    def subir_nivel(self):
        self.nivel += 1
        self.fuerza += 2
        self.magia += 1
        self.hp = self.fuerza * 5
        self.pm = self.magia * 5
        self.habilidad += 1
        self.carisma += 1


