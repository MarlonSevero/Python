"""
Herenca multipla.

Heranca multipla nada mais é do que a possibilidade de uma classe herdar de multiplas classes.
Fazendo que a classe filha herde todos os atributos e metodos de todas as classes herdadas.

ps. Uma classe deriva de outra quando ela herda de outra classe.

A heranca multlipla pode ser feita de duas maneiras:
    *Por multiderivacao direta:
    *Por multiderivacao indireta:


"""


class Animal:
    def __init__(self, name):
        self.__name = name


class Aquatico(Animal):
    def __init__(self, name):
        super().__init__(name)

    def swimming(self):
        return f'I am swiwmming {self._Animal__name}'

    def hello(self):
        return f'hello {self._Animal__name}'


class Terrestre(Animal):
    def __init__(self, name):
        super().__init__(name)

    def walking(self):
        return f'I am walking {self._Animal__name} '

    def hello(self):
        return f'hello {self._Animal__name}'


class Pinguim(Aquatico, Terrestre):     # A ordem importa no comportamento do objeto
    def __init__(self, name):
        super().__init__(name)


pux = Pinguim('Pux')
baleia = Aquatico('Baleia')

print(baleia.hello())
print(baleia.swimming())

tatu = Terrestre('Tatu')
print(tatu.walking())
print(tatu.hello())
print(pux.hello())
print(pux.walking())

#Objeto é instancia de:

print(isinstance(tatu, Terrestre))
print(isinstance(pux, Animal))
print(isinstance(pux, object))
print(isinstance(pux, Pinguim))


