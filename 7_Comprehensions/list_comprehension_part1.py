"""
List Comprehension

- Utilizando List Comprehension nós podemos gerar novas listas com dados processados a partir de outro
iterável.

# Sintaxe da List Comprehension:

[ dado for dado in iterável ] (Para cada dados nessa coleção de dados coloque esse dado para mim na 'tela'.
Dai podemos fazer somas, equações, funções, )

Iterável : Coleção de Dados.

#Exemplos

numeros = [1, 2, 3, 4, 5]

res = [numero * 10 for numero in numeros]
print(res)

Para entender melhor o que esta acontecendo devemos dividir a
expressão em duas partes. Sendo elas:

1° Parte: For numero in numeros
2° Parte: numero * 10

# Para cada 'numero' na lista de numeros. Multiplique o numero * 10
# e gere uma lista para mim desses numeros.

# Podia ser outra operação tambem:

res = [numero / 2 for numero in numeros]
print(res)

# Ou até mesmo usarmos um função:

def quadr(valor):
    return valor*valor

res = [quadr(numero) for numero in numeros]
print(res)

********** List Comprehension vs Loop *********

# Loop
numeros_dobrados = []

for numero in [1, 2, 3, 4, 5]:
    numeros_dobrados.append(numero*2)

# Maximo de Refatoramento

print(numeros_dobrados)

# List Comprehension:
print([numero * 2 for numero in [1, 2, 3, 4, 5]])

****** Isso é uma pratica de quem conhece Python Avançado. ********

# Outros Exemplos:

# 1
nome = 'Geek University'
print([letra.upper() for letra in nome])

# 2
def caixa_alta(nome):
    nome = nome.replace(nome[0], nome[0].upper())
    return nome

amigos = ['joao', 'marcos', 'gustavo']
print([caixa_alta(amigo) for amigo in amigos])

# 3
print([numero * 3 for numero in range(1, 10)])

# 4
print([bool(valor) for valor in [0, [], '', True, 3.14]])

# 5
print([str(numero) for numero in [1, 2, 3, 4, 5]])
"""

