"""
Dicionários

OBS: Em algumas linguagens de programação, os dicionários Python são conhecidos
por mapas.

Dicionários são coleção do tipo chave/valor.

[0, 1, 2] CHAVE
[1, 2, 3] VALOR

Dicionários são representados por chaves {}.

OBS: Sobre dicionários
    - Chave e valor são separados por dois pontos 'chave:valor';
    - Tanto chave quanto valor podem ser de qualquer tipo de dado;
    - Podemos misturar tipos de dados

    # Criação de dicionários

# Forma 1 (Mais comum)

paises = {'br': 'Brasil', 'eua':'Estados Unidos', 'py': 'Paraguai'} # Chave : Valor ou Key/value
print(paises)
print(type(paises))

# Forma 2 (Menos Comum)

paises = dict(br='Brasil', eau='Estados Unidos', py='Paraguay')

print(paises)
print(type(paises))

# Acessando elementos

# Forma 1 - Acessando via chave, da mesma forma que lista/tupla
# ps:dicionários não são indexados

print(paises['br'])
# print(paises['ru'])

# OBS: Caso tentamos fazer um acesso utilizando uma chave que não existe, teremos o erro KeyError

# Forma 2 - Acessando via get - Recomendada

print(paises.get('br'))
print(paises.get('ru'))

# Caso o get não encontre o objeto com a chave informada será retornado o valor None e não será gerado KeyError

pais = pais.get('ru')

if pais:
    print(f'Encontrei o país:{pais}')
else:
    print('Não encontrei o páis')

# Podemos definir um valor padrão para caso não encontremos o objeto com a chave informada
pais = pais.get('py', 'Nao encontrado')

print(f'Encontrei o país:{pais}')

# Podemos verificar se determinada chave se encontra em um dicionário. ps: Ele busca pela Chave.

print('br' in paises)
print('ru' in paises)
print('Estados Unidos' in paises)

# Podemos utilizar qualquer tipo de dado (int, float, string, boolean), inclusive lista, tupla dicionário, como
# chaves de dicionários.

# Tuplas são por exemplo são bastante interessantes de serem utilizadas como chave de dicionários,
# pois as mesmas são imutáveis.

localidades = {
    (35.6895, 39.7890): 'Escritório em Tókio',
    (47.6895, 74.0600): 'Escritório em Nova York',
    (89.6895, 125.2589): 'Escritório em Tókio',
}

print(localidades)
print(type(localidades))

# Adicionar elementos em um dicionários

receita = {'jan':100, 'fev': 120, 'mar': 300}

print(receita)
print(type(receita))

# Forma 1 - Mais comum

receita['abr'] = 350
print(receita)
# Forma 2

novo_dado = {'mai': 500}
receita.update(novo_dado) # receita.update({'mai':500})
print(receita)

# Atualizando dados em um dicionários

# Forma 1

receita['mai'] = 550
print(receita)

# Forma 2

receita.update({'mai': 600})
print(receita)

#estudar novamente isso
# CONCLUSÃO: A forma de adicionar novos elementos ou atualizar dados em um dicionário é a mesma
# CONCLUSÃO: Em dicionários, NÃO podemos ter chaves repetidas.

# Remover dados de um dicionário.

receita = {'jan':100, 'fev': 120, 'mar': 300}

print(receita)

# Forma 1 - Mais Comum

ret = receita.pop('mar')
print(ret)
print(receita)

# OBS 1: Aqui precisamos sempre informar a chave, e caso não encontre o elemeneto, um KeyError é retornado.
# OBS 2: Ao removermos um objeto, o valor deste objeto é sempre retornado.

# Forma 2

del receita['fev'] # del ETAR

print(receita)
del receita['fev']

# Se a chave não existir será gerado um KeyError
# OBS: Neste  caso o valor removido não é retornado.

# Imagine que vocẽ tem um comércio eletrõnico, onde temos um carrinho de compras no qual adicionamos produtos.

Carrinho;
	Produto 1;
		-nome;
		-quantidade;
		-preço;
	Produto 2;
		nome;
		quantidade;
		preço;


# 1- Poderiamos utilizar uma lista para isso?

carrinho = []

produto1 = ['PLaystation 4', 1, 1300.00]
produto2 = ['God Of War 4', 1, 150.00]

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)

# Terriamos que saber qual é o indice de cada informação no produto.

# 2 - Poderiamos utilizar uma tupla para isso? Sim

produto1('Playstation 4', 1, 1300.00)
produto2('God Of War 4', 1, 150.00)

carrinho = (produto1, produto2)

print(carrinho)

# Terriamos que saber qual é o indice de cada informação no produto.

# 3 - Poderiamos utilizar um dicionarios para isso? Sim  - Melhor maneira

carrinho = []

produto1 = {'nome': 'Playstation 4', 'quantidade': 1, 'preco': 2300.00}
produto2 = {'nome': 'God of War 4', 'quantidade': 1, 'preco': 150.00}

carrinho.append(produto1)
carrinho.append(produto2)

# Destas forma, facilmente adicionamos ou removemos produtos no carrinho e em cada produto
# podemos ter a certeza sobre cada informação

# As coleções se completam, nunca esqueça isso.

"""

"""
# Metodos de dicionarios

['__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribut
e__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '
__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'c
lear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']

# Limpar o dicionarios (Zerar dados)
d.clear()
print(d)

#Copiando um dicionario para outro

d = dict(a=1, b=2, c=3)
print(d)
print(type(d))

Forma 1 - Deep Copy

novo = d.copy()
print(novo)
novo['d'] = 4
print(d)
print(novo)

# Forma 2 - Shallow Copy

novo = d
print(novo)
novo['d'] = 50
print(novo)
print(d)

# O deep e shallow copy funcionam igual em qualquer sentido

# Forma não usal de criacao de dicionarios

outro = {}.fromkeys('a', 'b')
print(outro)
print(type(outro))

usuario = {}.fromkeys(['nome', 'pontos', 'email', 'profile'], 'desconhecido')
print(usuario)
print(type(usuario))

# O método fromkeys recebe dois parametros: um iteravel e um valor.
# Ele vai gerar para cada valor do iterável uma chave e irá atribuir a esta chave o valor informado.

veja = {}.fromkeys('teste', 'valor')
print(veja)

# Nao repete valor porque como vimos em dict python não temos repeticao de chave

veja = {}.fromkeys(range(1, 11), 'valor')
print(veja)
"""
from builtins import print




