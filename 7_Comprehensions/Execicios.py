"""
ex01.

words = ["Dada", "uma", "lista", "palavras", "crie", "pquletras"]
letters5 = []
letters = [letters5.append(word) for word in words if len(word) > 5]
print(letters5)

-

ex02.
numbers_par = []
num_par = [numbers_par.append(_) for _ in range(0, 1000) if _ % 2 == 0]
print(numbers_par)

ex03.
numbers = [num for num in range(1, 1000)]
numbers_par = [nums for nums in numbers if nums % 2 == 0]
print(numbers_par)

ex04.
words = ['Marlon', 'Allan', 'Joao', 'Augusto', 'amanda']
names = [name for name in words if name[0][0] == 'A' or name[0][0] == 'a']
print(names)

ex05.
words = ['Marlon', 'Allan', 'Joao', 'Augusto', 'amanda']
words_upper = [upper.upper() for upper in words]
print(words_upper)

ex06.
numbers = [num for num in range(0, 24556)]
less_ten = [print(lessen) for lessen in numbers if lessen < 10]


ex07.

words = ['Marlon', 'Allan', 'Joao', 'Augusto', 'amanda']
def wds(lsita):
    return print([num.__len__() for num in lsita])

ex08.

matriz2 = [[1, 2, 3], [4, 5, 6], [8, 9, 10]]

def soma_elementos(matriz):
    soma = sum(num for linha in matriz for num in linha)
    print(soma)

ex09. REFATORAR PARA COMPREHENSIONS

for indx in matriz2:
    for num in indx:
        soma = soma + num
    print(soma)

EX01: lAMBDAS
numbers = [x for x in range(0, 199)]
print(list(map(lambda y: y ** 2, numbers)))

EX02.
pessoas = [("Alice", 30), ("Bob", 25), ("Charlie", 35)]
ordered = sorted(pessoas, key = lambda x: x[1])

EX03.
words = ['a', 'b', 'c', 'd', 'e']
upper = list(map(lambda wd: wd.upper(), words))
print(upper)

EX04.

from functools import reduce

dados = [1, 2, 3, 4, 5]
def multi(numbers):
    return reduce(lambda x, y: x * y, numbers)


print(multi(dados))

"""

#print(list(map(lambda r: math.pi * (r ** 2), raios)))


def colore(texto, cor):
    if type(texto) is not str:
        raise TypeError("texto precisa ser uma string")
    if type(cor) is not str:
        raise TypeError("cor precisa ser uma string")
    print(f'O texto {texto} será impresso em {cor}')

colore(4, 'ola')


