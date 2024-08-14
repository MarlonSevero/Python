"""
*Args

Entendendo o *args

- O *args é um pararametro como outros qualquer ou seja de entrada. Isso significa que voce podera chamar
de qualquer coisa desde que comece com * 'Asterisco'

Exemplo:

*xis

Mas por convenção utilizamos *args para defini-lo

Mas o que é o *args

O parametro *args utilizado em uma função coloca os valores extras informados como
entrada em uma tupla. Então desde já lembre-se que tuplas são imutavei

Exemplo de como NÃO fazer:

def soma_todos_numeros(num1, num2, num3):
    return num1 + num2 + num3

print(soma_todos_numeros(4,6,9))

# print(soma_todos_numeros(4,6)) # TypeError
# print(soma_todos_numeros(4,6,9,7)) # TypeError

# Como é a maneira PROFISSIONAL de fazer

def soma_todos_numeros(*args):
    total = 0
    for numero in args:
        total = total + numero
    return total

# Ou Simplesmente

def soma_todoss_numeros(*args):
    return sum(args)

print(soma_todoss_numeros(1))
print(soma_todoss_numeros(1, 2))
print(soma_todos_numeros(1, 2, 3))

# *Args com outros tipos de dados

def soma_valores(nome, email, *args):
    return nome, email, sum(args)

print(soma_valores('Marlon', 'Salles', 10, 11))

#Outro exemplo de utilização do *args


def verifica_info(*args):
    if 'Geek' in args and 'University' in args:
        return 'Bem-Vindo Geek'
    return 'Nao te conheço'


print(verifica_info())
print(verifica_info(1, True, 'University', 'Geek'))
print(verifica_info('University', 3.145))

# Como *args é uma tupla, tudo que se aplica na tupla se aplica a ele.
# O *args extende o poder da nossa função

def soma_numeros(*args):
    return sum(args)

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros2 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

print(soma_numeros())
print(soma_numeros(1, 2, 3))  # Funciona Normalmente, porem se fizermos assim com listas teremos um TypeError
#print(soma_numeros(numeros))  #TypeError

# Desempacotador
print(type(numeros2))
print(soma_numeros(*numeros))
print(soma_numeros(*numeros2))

# OBS: O asterisco serve para que informemos ao Python que estamos passando como argumento
# uma coleção de dados. Desta forma ele saberá que precisará antes desempacotar esses dados.
# Tambem se aplica a dicionarios, SET
"""




