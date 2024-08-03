"""
Tuplas (tuple)

Tuplas são basicamente parecidas com listas.

Existem basicamente duas diferenças básicas:

1 - As tuplas são representadas por parênteses ()

print(type(()))

2 - As tuplas são imutáveis: Isso significa que ao se criar uma tupla ela não muda. Toda
operação em uma tupla gera uma nova tupla.

# Cuidado 1: As tuplas são representadas por ( ), mas veja:

tupla1 = (1, 2, 3, 4, 5, 6)
print(tupla1)

print((type(tupla1)))

tupla2 = 1, 2, 3, 4, 5, 6 ou ,
print(tupla2)

print(type(tupla2))

# CUIDADO 2: Tuplas com 1 elemento

tupla3 = (4) # Isso não é uma tupla !
print(tupla3)
print(type(tupla3))

tupla4 = (4,) # ou  4, Isso é uma tupla!
print(tupla4)
print(type(tupla4))

# CONCUSÃO: Podemos concluir que tuplas são definidas pela vírgula e não pelo uso de parênteses

(4) -> Não é tupla
(4, ) -> É tupla
4,-> É tupla

# Podemos gerar uma tupla dinamicamente com range(inicio,fim,passo)

tupla = tuple(range(11))
print(tupla)
print(type(tupla))

#Desenpacotamento de tupla

tupla = ('Geek', 'University',)
escola, curso = tupla
print(escola)
print(curso)

# OBS: Gera erro (ValueError) se colocarmos um número diferente de elementos para desenpacotar.

# Métodos para adição e remoção de elementos nas tuplas não existem, dado o fato das tuplas serem imutáveis.

# Soma*, Valor Maximo*, Valor Minimo* e Tamanho

# * Se os valores forem todos inteiros ou reais exceto 'len'

tupla = (1, 2, 3, 4, 5, 6,)

print(sum(tupla))
print(max(tupla))
print(min(tupla))
print(len(tupla))

# Concatenação de tuplas

tupla1 = (1, 2, 3)
print(tupla1)

tupla2 = (4, 5, 6,)
print(tupla2)

print(tupla1+tupla2) # Tuplas são imutáveis
print(tupla1)
print(tupla2)

tupla3 = tupla1 + tupla2
print(tupla3)
print(tupla2)
print(tupla1)

tupla1 = tupla1 + tupla2 # Tuplas são imutáveis, mas podemos sobrescrever seus valores.
print(tupla1)

# Verificar se determinado elemento está contido na tupla

tupla = 1, 2, 3,
print(3 in tupla) # Nao esqueça que tuplas são basicamente listas então isso é igual lá
# Iterando sobre uma tupla

# Verificar se determinado elemento está contido na tupla

tupla = 1, 2, 3,

for n in tupla:
    print(n)

for indice, valor in enumerate(tupla):
    print(indice, valor)

# Contando elementos dentro de uma tupla

tupla = ('a', 'b', 'c', 'd', 'e', 'a', 'b')
print(tupla.count('c'))

escola = tuple("Marlon Salles")

print(escola)

print(escola.count('a'))

# Dicas na utilização de tuplas

# Devemos utilizar tuplas SEMPRE que não precisarmos mudar os dados contidos em uma coleção

# Exemplos

meses = 'JANEIRO','FEVEREIRO','MARÇO','ABRIL','MAIO','JUNHO','JULHO','AGOSTO','SETEMBRO','OUTUBRO','NOVEMBRO','DEZEMBRO',

# Slicing

# Tupla[inicio:fim:passo]

print(meses[5:9])

print(meses)

# O acesso a elementos de uma tupla também é semelhante a de uma lista.
print(meses[5])

# Iterando com while
i = 0
while i < len(meses):
    print(meses[i])
    i = i + 1

# Verificamos em qual indice um elemento está na tupla

print(meses.index('JUNHO'))

# OBS: Caso o elemento não exista, será gerado ValueError.

# Por que utilizar tuplas?

# - Tuplas são mais rápidas do que listas.
# - Tuplas deixam seu código mais seguro*.

# *Isso porque trabalhar com elementos imutáveis traz segurança para o código

# Copiando uma tupla em outra

tupla = (1, 2, 3)
print(tupla)

nova = tupla  # Na tupla não temos o problema de Shallow Copy

print(nova)
print(tupla)

outra = 4, 5, 6

nova = nova + outra

print(nova)
print(outra)
print(tupla)

# ***Metodos com Tuplas***

print(dir(tuple))

['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__',
'__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__',
'__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__',
 '__sizeof__', '__str__', '__subclasshook__', 'count', 'index']
"""
