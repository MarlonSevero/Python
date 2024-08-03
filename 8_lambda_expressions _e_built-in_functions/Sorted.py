"""
Sorted

OBS: Nao confunda, apesar do nome, com a funcao sort() que ja estudamos em Listas.
O sort() so funciona em listas.

Podemos utilizar o sorted() com qualquer iteravel.

Como o proprio nome diz, sorted() serve para ordenar.

O sorted(), SEMPRE retorna uma Lista com os elementos do iteravel ordenados.

numeros = {5, 10, 11, 25, 4, 6}
print(numeros)

print(sorted(numeros))
print(numeros)

numeros = {5, 10, 11, 25, 4, 6}

print(sorted(numeros))
print(numeros)

# Adicionando parametros ao sorted()

print(sorted(numeros, reverse = True)) # Ordena do maior para o menor

# Podemos usar o sorted() para coisas mais complexas

# Imagine um twitter

usuarios = [
    {"username": "Samuel", "tweets": ["Eu adoro Bolos", "Eu adoro Pizzas"]},
    {"username": "Carla", "tweets": ["Eu amo meu Gato"]},
    {"username": "Aeff", "tweets": []},
    {"username": "Bob123", "tweets": []},
    {"username": "Doggo", "tweets": ["Eu gosto de Cachorros", "Eu Vou Sair hoje"]},
    {"username": "Gal", "tweets": [], 'cor': 'amarelo', 'musica': 'rock'}
]
print(usuarios)

print('************')

# Ordenando por username - Ordem Alfabetica
print(sorted(usuarios, key=lambda usuario: usuario['username']))

print('************')

# Ordenando pelo numero de tweets
print(sorted(usuarios, key=lambda usuario: len(usuario['tweets']),reverse=True))
"""




