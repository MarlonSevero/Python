"""
Map

Com Map, fazemos mapeamento de valores para função.

import math

def area(r):
    return math.pi * (r ** 2)

print(area(100))

raios = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
areas = []

# Forma Comum
for r in raios:
    areas.append(area(r))

print(areas)

# Forma 2 - Map
# Map é uma função que recebe dois parametros: O primeiro a função, o segundo um iterável. Retorna um Map Object

areas = map(area, raios)
print(areas)
print(type(areas))
print(list(areas))
print(list(map(area, raios))) # Mesma coisa com menas linhas de codigo.

# O Map mapeia uma função para um iterável. Ele vai pegar cada um dos dados do iterável e passar como entrada
# para a função. E claro colentando os resultados, os resultados vão ser armazenados no tipo de dado Map Object,
# O mesmo podemos converter para lista/tupla/dicionario/Set ..
# Geralmente não é passado uma função comum como acima, que esta informado a função 'area'.
# É mais comum ver sendo passado uma expressão Lambda no lugar da função. Como feito abaixo:

# Forma 3 - Map com Lambda
print(list(map(lambda r: math.pi * (r ** 2), raios)))

# OBS: Após utilizar a função map() depois da primeira utilização do resultado, ele zera.
# Isso é bacana porque limpa a memoria

print(list(areas))

**********  Para Fixar - Map  **********

# Temos dados iteráveis:

# dados: a1, a2, ..., an

# Temos uma função:

# Utilizamos a função map(f, dados) onde map irá 'mapear' cada elemento dos dados e aplicar a função.

# O map Object: f(a1), f(a2), f(...), f(an)

# Mais um exemplo

cidades = [('Berlim', 29), ('Cairo', 36), ('Buenos Aires', 19), ('Los Angeles', 26), ('Nova York', 28)]
print(cidades)

# f = 9/5 * c + 32

c_para_f = lambda dado: (dado[0], (9/5) * dado[1] + 32)
print(list(map(c_para_f, cidades)))
# Ou simplesmente
print(list(map(lambda dado: (dado[0], (9/5) * dado[1] + 32), cidades)))

# A função utilizada no Map Recebe um parametro.


"""








