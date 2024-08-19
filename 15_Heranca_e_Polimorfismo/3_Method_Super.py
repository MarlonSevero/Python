"""
Com super podemos acessar qualquer elemento na classe Pai


"""


class Animal:
    def __init__(self, nome, especie):
        self.nome = nome
        self.especie = especie

    def sound(self, sound):
        return f'O {self.nome} faz {sound}'


class Gato(Animal):
    def __init__(self, nome, especie, raca):
        #Animal.__init__(self, nome, especie) Nao recomendado
        super().__init__(nome, especie) #Com super() nao precisa do Self
        self.raca = raca

