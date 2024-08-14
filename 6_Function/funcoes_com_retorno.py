"""
Funções com retorno

numeros = [1, 2, 3]

ret_pop = numeros.pop()

print(f'retorno de pop: {ret_pop}')

FUNÇÃO SEM RETORNO

# Exemplo 1
ret_pr = print(numeros)
print(f'Retorno do Print: {ret_pr}')

#Exemplo 2 sem retorno

def quadrado_de_7():
    print(7*7)

ret = quadrado_de_7()
print(f'Retorno {ret}')

*************************************************

OBS : Em python quando uma função nao retorna nanhum valor, o retorno é None.

-> Refatorar = Reescrever para melhorar o codigo

-> Funções Python que retornam valores, devem retornar estes valores com a palavra reservada return

-> Não precisamos necessariamente criar uma variavel para receber o retorno de uma função. Podemos passar a
execução da função para outras funções.

***************************************************


# COM RETORNO

def quadrado_de_7():
    return 7*7

       # Criamos uma variavel para o retorno da função
ret = quadrado_de_7()

print(f'Retorno {ret}')

-> Podiamos simplismente fazer:

print({quadrado_de_7()+1})

obs:

Esta função,

def diz_oi():
    print('Oi')

é diferente desta,

def diz_oi():
    return 'Oi'

Tente sempre usar return!

****************OBS: Sobre a palavra reservada return*************

1 - Ela finaliza a função, ou seja, ela sai da execução da função;

# Exemplo 1

def diz_oi():
    print('antes')
    return 'oi'
    print('apos nd é executado')

print(diz_oi())

2 - Podemos ter, em uma função, diferentes returns;

# Exemplo

def nova_funcao():
    var = False
    if var:
        return 4
    elif var is None:
        return 3.2
    return 'b'

print(nova_funcao())

**3 - Podemos, em uma função, retornar qualquer tipo de dado e até mesmo multiplós valores;**

# Exemplo

def outra_funcao():
    return 2, 3, 4, 5

print(outra_funcao())
print(type(outra_funcao()))

ou

#num1, num2, num3, num4 = outra_funcao() - desempacotando a tupla caso necessario
#print(num1, num2, num3, num4)

# Erros comuns na utilização do retorno, que na verdade nem é erro, mas sim codificação desnecessária

def e_impar():
    num = 5
    if num % 2 != 0:
        return True # NAO COLOQUE O ELSE SEM NECESSIDADE
    return False

print(e_impar())
"""

# Vamos criar uma função para jogar a moeda

from random import random # - Pacote da função Random da Biblioteca Py


def joga_moeda():
    # Gera um numero pseudo_randomico (Aleatorios entre 0 e 1)
    # pseudo - sub-entendido que vai haver repetição
    if random() > 0.5:
        return 'Cara'
    return 'Coroa'

print(joga_moeda())

