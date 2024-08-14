"""
Listas

Listas em Python funcionam como vetores/matrizes (arrays) em outras linguagens, com a diferença
de serem DINÂMICO e também de podermos colocar QUALQUER tipo de dado.

Linguagens C/Java: Arrays
    -Possuem tamanho e tipo de dado fixo;
    Ou seja, nestas linguagens se você criar um array do tipo int e com tamanho 5, este array
    será SEMPRE do tipo inteiro e poderá ter sempre no máximo 5 valores.

Já em Python:

- Dinâmico: Não possuem tamanho fixo; Ou seja, podemos criar a lista e simplismente ir adicionando elementos;
- Qualquer tipo de dado: Não possuem tipo de fafo fixo; Ou seja, podemos colocar qualquer tipo de dado;

As listas em Python são representadas por colchetes: []
type([])

********

lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]

lista2 = ['M', 'A', 'R', 'L', 'O', 'N']

lista3 = []

lista4 = range(11)

lista5 = list('MARLON')

# Podemos facilmente converter uma string para uma lista

# Exemplo 1

curso = 'Pogramação em Python para ser Rich'

print(curso)
curso = curso.split()
print(curso)

# OBS: Por padrâo, o split separa os elementos da lista pelo espaço entre elas.

# Exemplo 2
curso = 'Programação,em,Python,para ser,Rich'
print(curso)
curso = curso.split(',')
print(curso)

********

# Convertendo uma lista em uma string
lista6 = ['Programação', 'em', 'Python']
print(lista6)

# Abaixo estamos falando: Pega a lista6, coloca espaço entre cada elemento e transforma em uma string
curso = ' '.join(lista6)
print(curso)
# Abaixo estamos falando: Pega a lista6, coloca cifrão entre cada elemento e transforma em uma string
curso = '$'.join(lista6)
print(curso)

#Podemos realmente colocar qualquer tipo de dado em uma lista, inclusive misturando esses dados.

lista6 = [1, 2, 34, True, 'Geek', 'd', [1, 2, 3], 14154566365685214]
print(lista6)
print(type(lista6))

********

# Iterando sobre listas

#Exemplo 1 - Utilizando for

soma = 0
for elemento in lista1:
    print(elemento)
    soma = soma + elemento
print(f'A soma dos valores dessa lista é: {soma}')

# Exemplo 2 - Utilizando while

carrinho = []
produto = ''

while produto != 'sair':
    print("Adicione um produto na lista ou digite 'sair' para sair: ")
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)

for produto in carrinho:
    print(produto)

********
/
# Utilizando variáveis em listas
numeros = [1, 2, 3, 4, 5]
print(numeros)

num1 = 1
num2 = 2
num3 = 3
num4 = 4
num5 = 5
numeros             = [num1, num2, num3, num4, num5]
print(numeros)

********

# Fazemos acesso aos elementos de forma indexada
#            0         1        2        3
cores = ['verde', 'amarelo', 'azul', 'branco']
print(cores[0]) #Verde
print(cores[1]) #Amarelo
print(cores[2]) #Azul
print(cores[3]) #Branco

# Fazer acesso aos elementos de forma indexada inversa
# Para entender melhor o índice negativo, pense na lista como um círculo, onde
# o final de um elemento esté ligado ao inicio da lista

print(cores[-1]) # Branco
print(cores[-2]) # Azul
print(cores[-3]) # Amarelo
print(cores[-4]) # Verde

# print(cores[-5]) # Erro, pois não existe indice -5
for cor in cores:
    print(cor)

indice = 0
while indice < len(cores):
    print(indice)
    indice = indice + 1

********

# Gerar indice em um for mostrando o numero da lista  que o valores está contido

for indice, cor in enumerate(cores):
    print(indice, cor)

# Listas aceitam valores repetidos

lista = []
lista.append(23)
lista.append(23)
lista.append(33)
print(lista)

****************

# Outros métodos não tão importantes mas também úteis

# Encontrar o indice de um elemento na lista

numeros = [7, 6, 5, 7, 9, 10, 7]
#Em qual indice da lista está o valor 6
print(numeros.index(6))

#Em qual indice da lista está o valor 9
print(numeros.index(9))

# print(numeros.index(19)) #Gera ValueError

# OBS: Caso não tenha este elemento na lista, será apresentado erro ValueError

# OBS: Retorna o indice do primeiro elemento encontrado
print(numeros.index(7))

#Podemos fazer busca dentro de um range, ou seja, qual indice começar a buscar
print(numeros.index(7, 1)) #Buscando a partir do índice 1
print(numeros.index(7, 2)) #Buscando a partir do índice 2
print(numeros.index(7, 3)) #Buscando a partir do índice 3
# print(numeros.index(7, 4)) #Buscando a partir do índice 4
# OBS: Caso não tenha este elemento na lista, será apresentado erro ValueError

# Podemos fazer busca dentro de um range, inicio/fim
print(numeros.index(10, 2, 6)) # Busca o indice do valor 10, entre os indices 2 a 6

********

# Revisão de slicing

# lista[inicio:fim:passo]
# range[inicio:fim:passo]

# Trabalhando com slice de lista com o parâmetro 'inicio'

lista = [1, 2, 3, 4]

print(lista[1:]) # Iniciando no índice 1 e pegando todos os elementos restantes ps:LEMBRA DO CIRCULO

# Trabalhando com slice de lista com o parâmetro 'fim'

print(lista[:2]) # começa em 0, pega até o indice 2 - 1
print(lista[:4]) # começa em 0, pega até o indice 4 - 1
print(lista[1:3]) # começa em 0, pega até o indice 3 - 1
#Negativo tambem funciona
print(lista[-4:-1])

# Trabalhando com slice de lista com o parâmetro 'passo'
print(lista[1::2]) # Começa em 1, vai até o final, de 2 em 2
print(lista[::2]) # Começa em 0, vai até o final, de 2 em 2

********

# Invertendo valores em uma lista

nome = "PROGRAMAÇÃO EM PYTHON"
print(nome[::-1])

nomes = ['joao', 'maria', 'jose']
print(nomes)
#modo pythonico
nomes.reverse()
print(nomes)

********

# Soma*, Valor Maximo, Valor Mínimo, Tamanho

# Se os valores forem todos inteiros ou reais.

lista = [1, 2, 3, 4, 5, 6]
print(sum(lista)) # soma
print(max(lista)) # máximo valor
print(min(lista)) # minimo valor
print(len(lista)) # tamanho da lista

********

#Transformar uma lista em tupla
lista = [1, 2, 3, 4, 5, 6]
print(lista)
print(type(lista))

tupla = tuple(lista)
print(tupla)
print(type(tupla))

# Desenpacotamento de Listas

lista = [1, 2, 3]
num1, num2, num3 = lista

print(num1)
print(num2)
print(num3)

# OBS: Se tivermos um numero diferente de  elementos na lista ou variaveis para receber os dados, teremos ValueError

# Copiando uma lista para outra {Shallow Copy e Deep Copy}

# Forma 1 - Deep Copy

lista = [1, 2, 3]
print(lista)

nova = lista.copy() #cópia

print(nova)

nova.append(4)

print(lista)
print(nova)

# Veja que ao utilizarmos lista.copy() copiamos os dados da lista para uma nova lista, mas elas
# ficaram totalmente independentes, ou seja, modificando uma lista , não afeta a outra. Isso em
# Python é chamado de Deep Copy (cópia profunda)

# Forma 2 - Shallow Copy

lista = [1, 2, 3]
print(lista)
nova = lista #copia

print(nova)
nova.append(4)
print(lista)
print(nova)

# Veja que utilizamos a cópia via atribuição e copiamos os dados da lista para a nova lista, mas
# após realizar modificação em uma das listas, essa modificação se refletiu em ambas as listas.
# Isso em Python é chamado de Shallow Copy.


***# Metodos com Listas***
print(dir([]))

['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__',
'__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init
_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__',
'__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__',
'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

"""
