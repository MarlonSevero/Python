"""
Generators Expressions

Em aulas anteriores nos estudamos:
- List Comprehensions;
- Dictionary Comprehensions;
- Set Comprehensions;

Nao vimos:
- Tuple Comprahensions....porque elas se chamam Generators

# Diferenca entre eles Comprehensions & Generators:

nomes = ['Camila', 'Carlos', 'Carla', 'Vanessa']

- List Comprehensions

res = [nome[0] == 'C' for nome in nomes]
print(type(res))

# Generator
res = (nome[0] == 'C' for nome in nomes)
print(type(res))

# O Genarator ocupa menos recursa da memoria. O Generator e sempre mais performatico.


# Qual e a utilidade de getsizeof()?
# -> Retorna a quantidade de bytes em memoria do elemento passado como parametro.

# Mostra quantos bytes a string 'Geek' esta ocupando em memoria. Quanto maior a string, mais
# espaco ocupa.

print(getsizeof('Geek'))
print(getsizeof('Geeeeeeeek'))
print(getsizeof(9))
print(getsizeof(90))
print(getsizeof(90151651652))
print(getsizeof(True))

# Gerando a mesma tarefa de diferentes maneiras comparando a eficiencia

# Gerando uma lista de numeros com List Comprehensions
list_comp = getsizeof([x * 10 for x in range(1000)])

# Gerando uma lista de numeros com Set Comprehensions
set_comp = getsizeof({x * 10 for x in range(1000)})

# Gerando uma lista de numeros com Dicionary Comprehensions
dic_comp = getsizeof({x: x * 10 for x in range(1000)})

# Gerando uma lista de numeros com Generators
gen = getsizeof(x * 10 for x in range(1000))

print('Para fazer a mesma tarefa gastamos em memoria:')
print(f'List Comprahension: {list_comp} bytes')
print(f'Set Comprahension: {set_comp} bytes')
print(f'Dicionary Comprahension: {dic_comp} bytes')
print(f'Generator Expression: {gen} bytes') # Nao guarda em memoria, somente quando usar

# Eu posso iterar o Generator Expression ? Sim

gen = (x * 10 for x in range(1000))
for n in gen:
    print(n)
"""

