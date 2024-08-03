"""
Set Comprehension

Lista = [1, 2, 3, 4, 5]
set = {1, 2, 3, 4, 5}

# Lembrando que SET não tem repetição de valores e nem ordenação.

# Exemplos

numeros = {num for num in range(10)}
print(numeros)

# Exemplos 2

numeros2 = {num ** 2 for num in range(10)}
print(numeros2)

# DESAFIO! : Faça uma alteração na estrutura acima para gerar um dicionario. Ao inves de SET.

numeros2 = {num: num ** 2 for num in range(10)}
print(numeros2)

# Exemplo 3

letras = {letra for letra in 'Marlon Salles'}
print(letras)

"""

