"""
**************Funções com Parametro (de Entrada)****************

- Funções que recebem dados para serem processados dentro da mesma;

Se a gente pensar em um programa qualquer, geralmente temos:

entrada -> processamento -> saída

Se a gente pensar em uma função, já sabemos que temos funções que:
- Não possuem entrada;
- Não possuem saída;
- Possuem entrada mas não possuem sáida;
- Não possuem entrada mas possuem saída;
- Possuem entrada e saída;

****** # Refatorando uma função ********

def quadrado(numero):
    return numero ** 2

EX 1 -
print(quadrado(49))

EX 2 -
ret = quadrado(7)
print(ret)

EX 3 -
print(quadrado()) # TypeError

**********************************

# Funcoes podem ter 'n' parâmetros de entrada. Ou seja, podemos receber como entrada
# em uma função quantos parâmetros forem necessários. Eles são separados por vírcula.

*********************************

****# Exemplos********

def soma(a, b):
    return a + b

def mult(num1, num2):
    return num1 * num2


def outra(num1, b, msg):
    return (num1 + b) * msg

print(soma(1, 6)) # Argumentos (a = 1)
print(soma(10, 20))

print(mult(4, 5))
print(mult(4, 8))

print(outra(2, 7, 'marlon '))
print(outra(3, 2, 'Geek '))

# OBS: Se a gente informar um numero errado de parêmetro ou argumentos. Teremos TypeError.

# print(soma(1, 2, 4)) # TypeError - Passando argumento a mais
# print(soma(1 )) # TypeError - Passando argumento a menos

***** # Nomeando parâmetros ********


def nome_completo(nome, sobrenome):
    return f'Seu nome completo é {nome} {sobrenome}'

print(nome_completo('Marlon', 'Salles'))

************# A diferença entre Parâmetros e Argumentos***********

# Parametros são variaveis declaradas na definição de uma função;
# Argumentos são dados passados durante a execução de uma função;

# A ordem dos parametros importa!

nome = 'Marlon'
sobrenome = 'Severo'

print(nome_completo(sobrenome, nome))

********# Argumentos Nomeados (Keyword Arguments)**********

# Caso utilizemos nomes dos parametros nos argumentos para informa-los, podemos
# utilizar qualquer ordem.

print(nome_completo(nome='Marlon', sobrenome='Salles'))
print(nome_completo(nome=nome, sobrenome=sobrenome))
print(nome_completo(sobrenome='Marques', nome='Marcia'))

********# Erros cumuns na utilização do return***********

def soma_impares(numeros):
    total = 0
    for num in numeros:
        if num % 2 != 0:
            total = total + num
    return total


lista = [1, 2, 3, 4, 5, 6, 7]
print(soma_impares(lista))

"""

