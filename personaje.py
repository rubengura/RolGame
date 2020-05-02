class Personaje:
    def __init__(self, nombre):
        self.nombre = nombre
        self.hp = 100
        self.pm = 50
        self.fuerza = 20
        self.habilidad = 15
        self.carisma = 15
        self.nivel = 1

    def subir_nivel(self):
        self.nivel += 1
        self.hp = int(self.hp * 1.10)
        self.pm = int(self.pm * 1.05)
        self.fuerza += 2
        self.habilidad += 1
        self.carisma += 1
