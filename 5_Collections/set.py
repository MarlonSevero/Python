"""
- Conjuntos

- Conjuntos em qualquer linguagem de programaçao, estamos fazendo referencia á Teoria dos Conjuntos
da Matemática

- Aqui no Python os conjuntos são chamados de Sets.

Dito isso, da mesma forma que na matematica:

- Sets (conjuntos) não possuem valores duplicados;
- Sets (conjuntos) não possuem valores ordenados;
- Elementos não são acessados via indice, ou seja, conjuntos nao sao indexados;

Conjuntos sao bons para se utilizar quando precisamos armazenar elementos
mas não nos importamos com a ordenacao deles. Quando nao precisamos se preocupar
com chaves, valores e itens duplicados.

Os conjutos {Sets} são referenciados em Python com chaves {}

Diferença entre Conjutos (Sets) e Mapas (Dicionarios) em Python:
    -Um dicionario tem chave/valor
    -Um conjunto tem apenas valor;

# Definindo um Conjunto:

# Forma 1

s = set({1, 2, 3, 4, 5, 6, 7, 2, 3}) # Repare que temos valores repetidos.

print(s)
print(type(s))

# OBS: Ao criar um conjunto, caso seja adicionado um valor já existente, o mesmo
# será ignorado sem gerar error e não fará parte do conjunto.

# Forma 2 - Mais Comum
s = {1, 2, 13, 4, 5, 6, 7, 2, 13}
print(s)
print(type(s))

# Podemos verificar se determinado elemento esta contido no conjunto
if 3 in s:
    print('Tem o 3')
else:
    print('Nao tem o 3')

# Importante lembrar que nao temos valores duplicados, nao temos ordem

# Lista aceitam valores duplicados, entao temos 10 elementos
lista = [99, 22, 34, 34, 1, 1, 5, 6, 7, 9]
print(f'lista: {lista} com {len(lista)} elementos')

# Tuplas aceitam valores duplicados, entao temos 10 elementos
tupla = (99, 22, 34, 34, 1, 1, 5, 6, 7, 9)
print(f'tupla {tupla} com {len(tupla)} elementos')

# Dicionarios nao aceitam chaves duplicadas, entao temos 8 elementos
dicionario = {}.fromkeys([99, 22, 34, 34, 1, 1, 5, 6, 7, 9], 'dict')
print(f'Dicionario: {dicionario} com {len(dicionario)} elementos')

# Conjuntos nao aceitam valores duplicados, entao temos 8 elementos
conjunto = {99, 22, 34, 34, 1, 1, 5, 6, 7, 9}
print(f'conjunto: {conjunto} com {len(conjunto)} elementos') # O conjunto faz a alto ordenação

# Assim como todo outro conjunto python podemos colocar todos os tipos de dados miscturados em Sets

s = {1, 'b', True, 34, 22, 44}
print(s)
print(type(s))

# Podemos iterar em um set normalmente

for valor in s:
    print(valor)

# Usos interessantes com sets

# Imagine que fizemos um formulario de cadastro de visitantes em uma feira ou museu e os visitantes
# informam manualmente a cidade de onde vieram

# Nos adicionamos cada cidade em uma lista Python, já que em uma lista podemos adicionar novos elementos
# e ter repetição.

cidades = ['Belo Horizonte', 'Sao paulo', 'Campo Grande', 'Cuiaba', 'Belo Horizonte', 'Campo Grande', 'Sao paulo']

print(cidades)
print(len(cidades))

# Agora precisamos saber, quantas cidades distintas, ou seja, unicas, temos.

# O que voce faria? Faria um loop na lista....?

# Podemos utilizar o set para isso:
print(len(set(cidades)))

# Adicionando elementos em um conjunto

s = {1, 2, 3}
s.add(4)
s.add(4) # Duplicidade nao gera erro. Simplesmente é ignorado e não é adicionado
print(s)

s = {1, 2, 3}
print(s)

# Forma 1

s.remove(3)  # NAO é indice! Informamos o valor a ser removido.

print(s)

# OBS: Caso o valor nao seja encontrado será gerado o erro KeyError. Nenhum valor é retornado

# Forma 2

s.discard(22)
print(s)

# OBS: Se o valor nao for encontrado nenhum erro é gerado.

s = {1, 2, 3}
print(s)

# Copiando um conjunto para outro...

# Forma 1 - Deep Copy

novo = s.copy()
print(novo)

novo.add(4)

print(novo)
print(s)

# Elementos Independentes um do outro

# Forma 2 - Shallow Copy

novo = s

novo.add(4)

print(novo)
print(s)

# Podemos remover todos os itens de um conjunto

s.clear()
print(s)

# Métodos matematicos de conjuntos.

# Imagine que temos dois conjuntos: um contento estudantes do curso Python e um
# contendo estudantes do curso de Java.

estudantes_python = {'Marcos', 'Patricia', 'Ellen', 'Pedro', 'Julia', 'Guilherme'}
estudantes_java = {'Gustavo', 'Patricia', 'Fernando', 'Ana', 'Julia'}

# Precisamos gerar um conjunto com nomes de estudantes unicos.

# Forma 1 - Utilizando union - recomendado

# union - União da Matematica ' U '

unicos = estudantes_python.union(estudantes_java)
print(unicos)

unicos = estudantes_java.union(estudantes_python)
print(unicos)
# - É a mesma coisa

# Forma 2 - Utilizando o caractere pipe |
unicos2 = estudantes_python | estudantes_java

print(unicos2)

# Veja que alguns alunos que estudam Python tambem estudam Java.

# Gerar um conjunto de estudantes que estao em ambos os cursos

# Forma 1 - Utilizando  intersection

# intersection  - Intersecção da Matematica ' ∩ '

ambos1 = estudantes_python.intersection(estudantes_java)
print(ambos1)

# Forma 2 - Utilizando o & ' E COMERCIAL '
ambos2 = estudantes_python & estudantes_java
print(ambos2)

# Gerar um conjunto de estudantes que não estao no outro curso

# difference  - Diferença (subtração) da Matematica ' - '

just_python = estudantes_python.difference(estudantes_java)
print(just_python)
just_java = estudantes_java.difference(estudantes_python)
print(just_java)

# Soma*, Valor Maxima*, Valor Minimo*, Tamanho

# * Se os valores forem todos inteiros e reais.

s = {1, 2, 3, 4, 5, 6, 7}
print(sum(s))
print(max(s))
print(min(s))
print(len(s))

s = {1, 2, 3, 4, 5, 6, 7}

dir(s) - Métodos

['__and__', '__class__', '__contains__', '__delattr__', '__dir__
', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute_
_', '__gt__', '__hash__', '__iand__', '__init__', '__init_subcla
ss__', '__ior__', '__isub__', '__iter__', '__ixor__', '__le__',
'__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__',
'__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__'
, '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__',
 '__subclasshook__', '__xor__', 'add', 'clear', 'copy', 'differe
nce', 'difference_update', 'discard', 'intersection', 'intersect
ion_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'rem
ove', 'symmetric_difference', 'symmetric_difference_update', 'un
ion', 'update']

"""

















