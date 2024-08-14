"""
Dictionary Comprehension

Pense no seguinte:

Dicionario -> {'a' : 1, 'b' : 2, 'c' : 3} #Chave e valor

Sintaxe:

{chave:valor for valor in iterável} -> Dictionary Comprehension
[valor for for in iteravel] -> List Comprehension

# Exemplos 1

numeros = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
quadrado = {chave: valor**2 for chave, valor in numeros.items()}
print(quadrado)

# numeros.items() transforma o dicionario em um lista de tuplas.
# Para cada chave e valor dentro dessa tupla, pegue a chave e multiple o valor ao quadrado.
# A chave não estamos mudando

#Exemplo 2 .items
teste = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
print(teste.items())
help(dict)

# Exemplo 3
lista = [1, 2, 3, 4, 5, 1, 2]

quadrado = {valor: valor**2 for valor in lista}
print(quadrado)

# Lembrando que não tem repetição de chave

# Exemplo 4

chaves = 'zyxwv' # String
valores = [1, 2, 3, 4, 5] # Lista
mistura = {chaves[i]: valores[i] for i in range(0, len(chaves))} # Dictionary Comprehensions
print(mistura)

# Exemplo 5 com Lógica Condicional

numeros = [1, 2, 3, 4, 5]
res = {num:('Par' if num % 2 == 0 else 'Impar') for num in numeros}
print(res)

********** Tudo que se aplica na List Comprehension se aplica aqui tambem. a unica diferença é que
invez de usarmos couchetes usamos chaves. *************

"""

notas = [100, 80, 60, 70, 80, 65]
alunos = ['Joao', 'Mario', 'Eduarda', 'Marcelo', 'Lucas', 'Roberto']

res = {alunos[i]: notas[i] for i in range(0, len(alunos))}
print(res)
