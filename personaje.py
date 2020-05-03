class Personaje:
    def __init__(self, nombre):
        self.nombre = nombre
        self.nivel = 1
        self.fuerza = 20
        self.magia = 10
        self.habilidad = 15
        self.carisma = 15
        self.max_hp = self.fuerza * 5
        self.max_pm = self.magia * 5
        self.hp_actuales = self.max_hp
        self.mp_actuales = self.max_pm
        self.capacidad_peso = self.fuerza * 3
        self.exp_acumulada = 0

    def subir_nivel(self):
        self.nivel += 1
        self.fuerza += 2
        self.magia += 1
        self.habilidad += 1
        self.carisma += 1
        self.max_hp = self.fuerza * 5
        self.max_pm = self.magia * 5
        self.capacidad_peso = self.fuerza * 3
