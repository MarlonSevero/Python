""""
List Comprehension

Nós podemos adicionar estraturas condicionais logicas ás nossas List Comprehension

# Exemplo 1

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

num_par = [numero for numero in numeros if numero % 2 == 0]
num_imp = [numero for numero in numeros if numero % 2 != 0]
print(num_par)
print(num_imp)

# Refatorando
# Qualquer numero Par módulo de 2 é 0 e 0 em Python é False. not false = True
num_par = [numero for numero in numeros if not numero % 2]
num_imp = [numero for numero in numeros if numero % 2]
print(num_par)
print(num_imp)

#Exemplo 2
res = [numero * 2 if numero % 2 == 0 else numero / 2 for numero in numeros]
print(res)

"""

res = [numero * 2 if numero % 2 == 0 else numero / 2 for numero in numeros]
