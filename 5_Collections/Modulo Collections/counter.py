from collections import Counter


"""
Módulo Collections - Counter (Contador)

Collections -> High-performace Container Datatype

Couter -> Recebe um iterável como parâmetro e cria um objeto do tipo Collections Counter que é parecido
com um dicionário, contento como chave o elemento da lista passado como parametro e como valor a quantidade
de ocorrências desse elemento.

# Realizando o import

from collections import Counter

# Exemplo 1

# Podemos utilizar qualquer iteravel, aqui usamos uma lista
lista = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 45, 55, 68, 68, 14]

# Utilizando o Counter
res = Counter(lista)
print(type(res))
print(res)

# Counter({1: 3, 2: 3, 3: 3, 4: 3, 5: 2, 68: 2, 45: 1, 55: 1, 14: 1})

# Veja que, para cada elemento da lista, o Counter criou uma chave e colocou como valor a quantidade de ocorrências.

# Exemplo 2

print(Counter('Marlon Salles Severo'))
# Para cada caracter ele criou uma chave, e colocou como valor a quantidade de ocorrências.
# Counter({'l': 3, 'e': 3, 'a': 2, 'r': 2, 'o': 2, ' ': 2, 'S': 2, 'M': 1, 'n': 1, 's': 1, 'v': 1})

from collections import Counter

texto = São formatos de arquivos de áudio. MID e WAV já já foram muito usados, mas recentemente com
o surgimento do MP3, este último acabou se tornando um modelo mais atraente já que consegue uma
compactação muito grande reduzindo o tamanho do arquivo sem grandes perdas de qualidade

palavras = texto.split()
# print(palavras)

res = Counter(palavras)

print(res)

# Encontrando as 5 palavras com mais ocorrencias no texto.
# most_common - mais comum
print(res.most_common(2))



 ALL DOCUMENTATION COUNTER

**** help(Counter) ****

Help on class Counter in module collections:

class Counter(builtins.dict)
 |  Counter(*args, **kwds)
 |
 |  Dict subclass for counting hashable items.  Sometimes called a bag
 |  or multiset.  Elements are stored as dictionary keys and their counts
 |  are stored as dictionary values.
 |
 |  >>> c = Counter('abcdeabcdabcaba')  # count elements from a string
 |
 |  >>> c.most_common(3)                # three most common elements
 |  [('a', 5), ('b', 4), ('c', 3)]
 |  >>> sorted(c)                       # list all unique elements
 |  ['a', 'b', 'c', 'd', 'e']
 |  >>> ''.join(sorted(c.elements()))   # list elements with repetitions
 |  'aaaaabbbbcccdde'
 |  >>> sum(c.values())                 # total of all counts
 |  15
 |
 |  >>> c['a']                          # count of letter 'a'
 |  5
 |  >>> for elem in 'shazam':           # update counts from an iterable
 |  ...     c[elem] += 1                # by adding 1 to each element's count
 |  >>> c['a']                          # now there are seven 'a'
 |  7
 |  >>> del c['b']                      # remove all 'b'
 |  >>> c['b']                          # now there are zero 'b'
 |  0
 |
 |  >>> d = Counter('simsalabim')       # make another counter
 |  >>> c.update(d)                     # add in the second counter
 |  >>> c['a']                          # now there are nine 'a'
 |  9
 |
 |  >>> c.clear()                       # empty the counter
 |  >>> c
 |  Counter()
 |
 |  Note:  If a count is set to zero or reduced to zero, it will remain
 |  in the counter until the entry is deleted or the counter is cleared:
 |
 |  >>> c = Counter('aaabbc')
 |  >>> c['b'] -= 2                     # reduce the count of 'b' by two
 |  >>> c.most_common()                 # 'b' is still in, but its count is zero
 |  [('a', 3), ('c', 1), ('b', 0)]
 |
 |  Method resolution order:
 |      Counter
 |      builtins.dict
 |      builtins.object
 |
 |  Methods defined here:
 |
 |  __add__(self, other)
 |      Add counts from two counters.
 |
 |      >>> Counter('abbb') + Counter('bcc')
 |      Counter({'b': 4, 'c': 2, 'a': 1})
 |
 |  __and__(self, other)
 |      Intersection is the minimum of corresponding counts.
 |
 |      >>> Counter('abbb') & Counter('bcc')
 |      Counter({'b': 1})
 |
 |  __delitem__(self, elem)
 |      Like dict.__delitem__() but does not raise KeyError for missing values.
 |
 |  __iadd__(self, other)
 |      Inplace add from another counter, keeping only positive counts.
 |
 |      >>> c = Counter('abbb')
 |      >>> c += Counter('bcc')
 |      >>> c
 |      Counter({'b': 4, 'c': 2, 'a': 1})
 |
 |  __iand__(self, other)
 |      Inplace intersection is the minimum of corresponding counts.
 |
 |      >>> c = Counter('abbb')
 |      >>> c &= Counter('bcc')
 |      >>> c
 |      Counter({'b': 1})
 |
 |  __init__(*args, **kwds)
 |      Create a new, empty Counter object.  And if given, count elements
 |      from an input iterable.  Or, initialize the count from another mapping
 |      of elements to their counts.
 |
 |      >>> c = Counter()                           # a new, empty counter
 |      >>> c = Counter('gallahad')                 # a new counter from an iterable
 |      >>> c = Counter({'a': 4, 'b': 2})           # a new counter from a mapping
 |      >>> c = Counter(a=4, b=2)                   # a new counter from keyword args
 |
 |  __ior__(self, other)
 |      Inplace union is the maximum of value from either counter.
 |
 |      >>> c = Counter('abbb')
 |      >>> c |= Counter('bcc')
 |      >>> c
 |      Counter({'b': 3, 'c': 2, 'a': 1})
 |
 |  __isub__(self, other)
 |      Inplace subtract counter, but keep only results with positive counts.
 |
 |      >>> c = Counter('abbbc')
 |      >>> c -= Counter('bccd')
 |      >>> c
 |      Counter({'b': 2, 'a': 1})
 |
 |  __missing__(self, key)
 |      The count of elements not in the Counter is zero.
 |
 |  __neg__(self)
 |      Subtracts from an empty counter.  Strips positive and zero counts,
 |      and flips the sign on negative counts.
 |
 |  __or__(self, other)
 |      Union is the maximum of value in either of the input counters.
 |
 |      >>> Counter('abbb') | Counter('bcc')
 |      Counter({'b': 3, 'c': 2, 'a': 1})
 |
 |  __pos__(self)
 |      Adds an empty counter, effectively stripping negative and zero counts
 |
 |  __reduce__(self)
 |      Helper for pickle.
 |
 |  __repr__(self)
 |      Return repr(self).
 |
 |  __sub__(self, other)
 |      Subtract count, but keep only results with positive counts.
 |
 |      >>> Counter('abbbc') - Counter('bccd')
 |      Counter({'b': 2, 'a': 1})
 |
 |  copy(self)
 |      Return a shallow copy.
 |
 |  elements(self)
 |      Iterator over elements repeating each as many times as its count.
 |
 |      >>> c = Counter('ABCABC')
 |      >>> sorted(c.elements())
 |      ['A', 'A', 'B', 'B', 'C', 'C']
 |
 |      # Knuth's example for prime factors of 1836:  2**2 * 3**3 * 17**1
 |      >>> prime_factors = Counter({2: 2, 3: 3, 17: 1})
 |      >>> product = 1
 |      >>> for factor in prime_factors.elements():     # loop over factors
 |      ...     product *= factor                       # and multiply them
 |      >>> product
 |      1836
 |
 |      Note, if an element's count has been set to zero or is a negative
 |      number, elements() will ignore it.
 |
 |  most_common(self, n=None)
 |      List the n most common elements and their counts from the most
 |      common to the least.  If n is None, then list all element counts.
 |
 |      >>> Counter('abcdeabcdabcaba').most_common(3)
 |      [('a', 5), ('b', 4), ('c', 3)]
 |
 |  subtract(*args, **kwds)
 |      Like dict.update() but subtracts counts instead of replacing them.
 |      Counts can be reduced below zero.  Both the inputs and outputs are
 |      allowed to contain zero and negative counts.
 |
 |      Source can be an iterable, a dictionary, or another Counter instance.
 |
 |      >>> c = Counter('which')
 |      >>> c.subtract('witch')             # subtract elements from another iterable
 |      >>> c.subtract(Counter('watch'))    # subtract elements from another counter
 |      >>> c['h']                          # 2 in which, minus 1 in witch, minus 1 in watch
 |      0
 |      >>> c['w']                          # 1 in which, minus 1 in witch, minus 1 in watch
 |      -1
 |
 |  update(*args, **kwds)
 |      Like dict.update() but add counts instead of replacing them.
 |
 |      Source can be an iterable, a dictionary, or another Counter instance.
 |
 |      >>> c = Counter('which')
 |      >>> c.update('witch')           # add elements from another iterable
 |      >>> d = Counter('watch')
 |      >>> c.update(d)                 # add elements from another counter
 |      >>> c['h']                      # four 'h' in which, witch, and watch
 |      4
 |
 |  ----------------------------------------------------------------------
 |  Class methods defined here:
 |
 |  fromkeys(iterable, v=None) from builtins.type
 |      Create a new dictionary with keys from iterable and values set to value.
 |
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |
 |  __dict__
 |      dictionary for instance variables (if defined)
 |
 |  __weakref__
 |      list of weak references to the object (if defined)
 |
 |  ----------------------------------------------------------------------
 |  Methods inherited from builtins.dict:
 |
 |  __contains__(self, key, /)
 |      True if the dictionary has the specified key, else False.
 |
 |  __eq__(self, value, /)
 |      Return self==value.
 |
 |  __ge__(self, value, /)
 |      Return self>=value.
 |
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |
 |  __getitem__(...)
 |      x.__getitem__(y) <==> x[y]
 |
 |  __gt__(self, value, /)
 |      Return self>value.
 |
 |  __iter__(self, /)
 |      Implement iter(self).
 |
 |  __le__(self, value, /)
 |      Return self<=value.
 |
 |  __len__(self, /)
 |      Return len(self).
 |
 |  __lt__(self, value, /)
 |      Return self<value.
 |
 |  __ne__(self, value, /)
 |      Return self!=value.
 |
 |  __setitem__(self, key, value, /)
 |      Set self[key] to value.
 |
 |  __sizeof__(...)
 |      D.__sizeof__() -> size of D in memory, in bytes
 |
 |  clear(...)
 |      D.clear() -> None.  Remove all items from D.
 |
 |  get(self, key, default=None, /)
 |      Return the value for key if key is in the dictionary, else default.
 |
 |  items(...)
 |      D.items() -> a set-like object providing a view on D's items
 |
 |  keys(...)
 |      D.keys() -> a set-like object providing a view on D's keys
 |
 |  pop(...)
 |      D.pop(k[,d]) -> v, remove specified key and return the corresponding value.
 |      If key is not found, d is returned if given, otherwise KeyError is raised
 |
 |  popitem(...)
 |      D.popitem() -> (k, v), remove and return some (key, value) pair as a
 |      2-tuple; but raise KeyError if D is empty.
 |
 |  setdefault(self, key, default=None, /)
 |      Insert key with a value of default if key is not in the dictionary.
 |
 |      Return the value for key if key is in the dictionary, else default.
 |
 |  values(...)
 |      D.values() -> an object providing a view on D's values
 |
 |  ----------------------------------------------------------------------
 |  Static methods inherited from builtins.dict:
 |
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |
 |  ----------------------------------------------------------------------
 |  Data and other attributes inherited from builtins.dict:
 |
 |  __hash__ = None

"""
lista = [1, 2, 3, 4, 5, 5, 5, 6]
res = Counter(lista)
print(type(res))
print(res)



