

class Carro:
    serial = 60060

    def __init__(self, marc, modelo, cor):
        self.serial = Carro.serial + 1
        self.marc = marc
        self.modelo = modelo
        self.cor = cor
        self.ligado = False
        Carro.serial = self.serial

    def turnon(self):
        x = int(input("Key 1 for turn on the car"))
        if x == 1:
            Carro.ligado = True
            print(f"Lest go, its the {Carro.ligado} position, Vrumm")
        else:
            print("Nada Aconteceu")

ford_onix = Carro("Ford", "Renauld", "Black")
ford_onix_10 = Carro("Ford", "Renauld 1.0", "Blue")

print(ford_onix.serial)
print(ford_onix_10.serial)
ford_onix.turnon()
