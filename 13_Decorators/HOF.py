"""
Higher Order Function (Funcoes de Maior Grandeza)

O que isso significa ?

    Quando uma linguagem de progracao, da suporte ao HOF indica que podemos ter funcoes que retorna outras funcoes
    como resultado.
    Ou mesmo, que podemos passar funcoes como parametros para outras funcoes.
    E tambem criar variaveis do tipo de funcoes do nosso programa.

    def summ(num1, num2):
        return num1 + num2

    def calc(num1, num2, function):             #Higher Function
        return function(num1, num2)

    print(calc(1, 10, summ))

#Nested Function

    Em python podemos ter funcoes dentro de funcoes, conhecidas como Nested Function ou Inner Function.

from random import choice

def hi(person_name):
    def humor():
        return choice(('Hello', 'Get Out', 'I love you'))
    return print(humor() + ' ' + person_name)


hi('Angelina')

from random import choice

def make_laugh():
    def laugh():
        return choice(('hahaha', 'kkkkkk', 'kdaskdaks'))
    return laugh()

rir = make_laugh()

print(rir)

"""



from random import choice

def make_laugh(person: str):
    def laugh():
        return choice(('hahaha', 'kkkkkk', 'kdaskdaks'))
    return person + ' ' + laugh()

rir = make_laugh('Angelina')

print(rir)





