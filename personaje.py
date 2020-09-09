arquetipo = {1: "Luchador", 2: "Mago", 3: "Pícaro"}


class Personaje:
    def __init__(self):
        nombre = input("¿Cómo se llama tu personaje?: ")
        jugador = input("¿Cómo te llamas tú?: ")
        input_arquetipo = input("""¿Qué clase deseas elegir?
1. Luchador
2. Mago
3. Pícaro""")

        self.arquetipo = arquetipo[int(input_arquetipo)]
        self.nombre = nombre
        self.jugador = jugador
        self.nivel = 1
        self.fuerza = 1
        self.habilidad = 1
        self.constitucion = 1
        self.percepcion = 1
        self.conocimiento = 1
        self.carisma = 1
        self.poder = 0
        self.lucha_fluida = 0
        self.lucha_contundente = 0

        self.inicializar_arquetipo()
        # self.max_hp = self.fuerza * 5
        # self.max_pm = self.magia * 5
        # self.hp_actuales = self.max_hp
        # self.mp_actuales = self.max_pm
        # self.capacidad_peso = self.fuerza * 3
        # self.exp_acumulada = 0
        # self.exp_proximo_nivel = 100

    # def subir_nivel(self):
    #     self.nivel += 1
    #     self.fuerza += 2
    #     self.magia += 1
    #     self.habilidad += 1
    #     self.carisma += 1
    #     self.max_hp = self.fuerza * 5
    #     self.max_pm = self.magia * 5
    #     self.capacidad_peso = self.fuerza * 3
    #     self.actualizar_exp_proximo_nivel()
    #
    # def adquirir_exp(self, puntos_exp):
    #     self.exp_acumulada += puntos_exp
    #     self.comprobar_nivel()
    #
    # def comprobar_nivel(self):
    #     if self.exp_acumulada >= self.exp_proximo_nivel:
    #         self.subir_nivel()
    #
    # # TODO
    # def actualizar_exp_proximo_nivel(self):
    #     pass

    def inicializar_arquetipo(self):
        if self.arquetipo == "Luchador":
            self.fuerza = 10
            self.conocimiento = 6
            self.poder = 2
        elif self.arquetipo == "Mago":
            self.fuerza = 2
            self.conocimiento = 7
            self.poder = 9
        elif self.arquetipo == "Pícaro":
            self.fuerza = 8
            self.conocimiento = 6
            self.poder = 4
