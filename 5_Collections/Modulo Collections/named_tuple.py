"""
Módulo Collections - Named Tuple

# Recap Tupla

tupla = (1, 2, 3)
print(tupla[1])

Named Tuple -> São tuplas, diferenciadas, onde, especificamos um nome para a mesma e tambem parâmetros.

# Importando

from collections import namedtuple

# Precisamos definir o nome e parâmetros

# Forma 1 - Declaração Named Tuple

cachorro = namedtuple('cachorro', 'idade raca nome')

# Forma 2 - Declaração Named Tuple

cachorro = namedtuple('cachorro', 'idade, raca, nome')

# Forma 3 - Declaração Named Tuple

cachorro = namedtuple('cachorro', ['idade', 'raca', 'nome']) # Recomendado

# Usando

ray = cachorro(idade=2, raca='Chow-Chow', nome='Ray')
print(ray)

# Acessando os dados

# Forma 1

print(f'A idade do cachorro é {ray[0]}')
print(f'O Raça do cachorro é {ray[1]}')
print(f'O nome do cachorro é {ray[2]}')

print('\n')

# Forma 2

print(f'A idade do cachorro é {ray.nome}')
print(f'O Raça do cachorro é {ray.raca}')
print(f'O nome do cachorro é {ray.nome}')

print(ray.index('Chow-Chow'))

# Ocorrencias
print(ray.count('Chow-Chow'))

# Tudo visto em tupla serve aqui!


ALL DOCUMENTATION NAMED TUPLE

**** help(namedtuple) ****

help(namedtuple)
Help on function namedtuple in module collections:

namedtuple(typename, field_names, *, rename=False, defaults=None, module=None)
    Returns a new subclass of tuple with named fields.

   Point = namedtuple('Point', ['x', 'y'])
 Point.__doc__                   # docstring for the new class
    'Point(x, y)'
    p = Point(11, y=22)             # instantiate with positional args or keywords
    p[0] + p[1]                     # indexable like a plain tuple
    33
    x, y = p                        # unpack like a regular tuple
    x, y
    (11, 22)
    p.x + p.y                       # fields also accessible by name
    33
    d = p._asdict()                 # convert to a dictionary
    d['x']
    11
    Point(**d)                      # convert from a dictionary
    Point(x=11, y=22)
    p._replace(x=100)               # _replace() is like str.replace() but targets named fields
    Point(x=100, y=22)

"""


