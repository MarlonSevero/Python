""""
Utilizando Lambdas

Conhecidas por Expressões Lambidas, ou simplesmente Lambdas, são funções sem nome, ou seja
funções anônimas.

# Função em Pythom
def funcao(x):
    return x * 3 + 1

print(funcao(10))

# Expressão Lambda
lambda x: 3 * x + 1

# Como utilizar a expressão L.ambda

calc = lambda x: 3 * x + 1
print(calc(7))

# Podemos ter expressões Lambdas com múltiplas entradas

nome_completo = lambda nome, sobrenome: nome.strip().title() +  ' ' + sobrenome.strip().title()
print(nome_completo('marlon   ', 'SaLlES             '))

# strip() - remove espaços no inicio e no fim da variavel
# Ajusta as letras

# Em funções python podemos ter nenhuma ou varias entradas, em Lambda tambem.

nenhuma = lambda: "Como nao ama Python?"
uma = lambda x: 3 * x + 1
duas = lambda x, y: (x*y)**0.5
tres = lambda x, y, z: 3/(1 / x+1 / y+1 / z)
# n = lambda x1, x2, x3, ....., xn <expressão>

print(nenhuma())
print(uma(7))
print(duas(10, 12))
print(tres(3, 6, 9))

# OBS: Se passarmos mais argumentos do que parâmetros esperados teremos TypeError

# Outro Exemplo

autores = ['Gustavo Aima', 'Jorge e Matheus', 'Pink Floyd', "Guns n' Roses", 'Metalicca','H. G. Hells']
print(autores)

autores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())
# [-1] em listas sempre vai pegar o ultimo elemento, como queremos olhar o
# ultimo nome utiliando ele na expressão lambda
# A FORMA CORRETA DE UTILIZAR LAMBDAS É DESSA MANEIRA, E NAO DECLARANDO EM VARIAVEIS.

print(autores)

# Função Quadrática

# a * x **2 + b * x + c

# Definindo a função


def funcao_quad(a, b, c):
    Retorna f(x) = a * x **2 + b * x + c
    return lambda x: a * x **2 + b * x + c

teste = funcao_quad(2, 3, -5)

print(teste(0))
print(teste(1))
print(teste(2))

print(funcao_quad(2, 3, -25)(0)) # Mesma coisa porém sem guardar em uma variavel.
"""
