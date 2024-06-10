
class Pokemon:

    def __init__(self, nombre, tipo, ataque, defensa, vida):
        self.nombre = nombre
        self.tipo = tipo
        self.ataque = ataque
        self.defensa = defensa
        self.vida = vida

    def mostrar_tipo(self):
        print("Tipo:", self.tipo)

    def usar_habilidad_especial(self):
        print(self.nombre, "ha usado una habilidad especial!")
        if self.tipo == "Fuego":
            print("¡Lanzó una bola de fuego!")
        elif self.tipo == "Agua":
            print("¡Generó una ola de agua!")
        elif self.tipo == "Planta":
            print("¡Invocó una enredadera!")
        else:
            print("Ninguna habilidad especial disponible para este tipo de Pokemon.")

    def atributos(self):
        print(f"Nombre: {self.nombre}")
        print(f"Ataque: {self.ataque}")
        print(f"Defensa: {self.defensa}")
        print(f"Vida: {self.vida}")
        print(f"Tipo: {self.tipo}")


pokemon_1 = Pokemon("Charizard", "Fuego", 60, 40, 70)
pokemon_2 = Pokemon("Blastoise", "Agua", 55, 45, 80)
pokemon_3 = Pokemon("Venusaur", "Planta", 50, 50, 75)

pokemon_1.atributos()
pokemon_2.atributos()
pokemon_3.atributos()

pokemon_1.usar_habilidad_especial()
pokemon_2.usar_habilidad_especial()
pokemon_3.usar_habilidad_especial()

