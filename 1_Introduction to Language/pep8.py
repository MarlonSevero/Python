"""
PEP - PYTHON ENHANCEMENT PROPOSALS
São propostas de melhorias para a linguagem Python

The Zen of Python - import this

PEP 8 -- Style Guide for Python Code --

A ideia da PEP8 é que possamos escrever códigos Python de forma Pythônica

[1] - Utilize Camel Case para nomes de classes;

class Calculadora:
    pass

class calculadora_cientifica:
    pass

ps: errado o certo seria CalculadoraCientifica

[2] - Utilize nomes em minusculo separados por underline para funções ou variaveis

def Soma():
    pass

def soma_dois():
    pass

numero = 4
numero_impar = 5

[3] - Utilize 4 espaços para indentação! Se não tiver indentado vai dar erro (Não use Tab )
if 'a' in 'banana':
    print ('tem a lepra A')

[4] - Linhas em Branco
-Separar funções e definições de classe com duas linhas em branco;
-Métodos dentro de uma classe devem ser separados com uma única linha em branco

class classe1:
    pass


class outraclasse
    pass

[5] - Imports

-Imports devem ser sempre feitos em linhas separadas;
# Import errado

import sys, os

#import certo

 import sys
 import os

 #Não há problemas em utilizadas :

 from types import StringType, ListType

 #Caso tenha muitos imports de um mesmo pacote, recomenda-se fazer:

 from types import(
    StringType,
    ListType,
    SetType,
    OutroType
 )

#Imports devem ser colocados no topo do arquivo, logo depois de quaisquer comentários ou docstrings e
#antes de constantes e variáveis globais

[6] - Espaços em expressões e instruções

#Não faça:
funcao(_algo[ 1 ], { outro: 2 } )

#Faça:
funcao(algo[1], {outro: 2})

#nao faça:
algo (1)

#faça:
algo(1)

#Não faça:
dict ['chave'] = list [indice]

#faca
dict['chave'] = lista[indice]

#n faca

x              = 1
y              = 3
variavel_longa = 5

[7] - Termine sempre uma instrução com uma nova linha

"""
import this
