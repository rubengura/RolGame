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
        self.exp_proximo_nivel = 100

    def subir_nivel(self):
        self.nivel += 1
        self.fuerza += 2
        self.magia += 1
        self.habilidad += 1
        self.carisma += 1
        self.max_hp = self.fuerza * 5
        self.max_pm = self.magia * 5
        self.capacidad_peso = self.fuerza * 3
        self.actualizar_exp_proximo_nivel()

    def adquirir_exp(self, puntos_exp):
        self.exp_acumulada += puntos_exp
        self.comprobar_nivel()

    def comprobar_nivel(self):
        if self.exp_acumulada >= self.exp_proximo_nivel:
            self.subir_nivel()

    # TODO
    def actualizar_exp_proximo_nivel(self):
        pass