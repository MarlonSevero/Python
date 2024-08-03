"""
Módulo Collections: Ordered Dict

# Em um dicionario, a ordem de inserção dos elementos não é garantida.
dicionarios = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

for chave, valor in dicionarios.items():
    print(f'chaves={chave}: valor={valor}')

OrderedDict -> É um dicionário, que nos garante a ordem de inserção dos elementos.

from collections import OrderedDict

dicionario = OrderedDict({'a': 1, 'b': 2, 'c': 3, 'd': 4})

for chave, valor in dicionario.items():
    print(f'chave={chave}: valor={valor}')

# Entendendo a diferença entre Dict e Ordered Dict

# Dicionarios comuns

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 2, 'a': 1}

print(dict1 == dict2) # True -> Já que a ordem dos elementos nao importa para os dicionarios

# Ordered Dict

from collections import OrderedDict

odict1 = OrderedDict({'a': 1, 'b': 2})
odict2 = OrderedDict({'b': 2, 'a': 1})

print(odict1 == odict2) # False -> Já que a ordem dos elementos importa para os OrderedDict


 ALL DOCUMENTATION ORDERED DICT

 help(OrderedDict)
Help on class OrderedDict in module collections:

class OrderedDict(builtins.dict)
 |  Dictionary that remembers insertion order
 |
 |  Method resolution order:
 |      OrderedDict
 |      builtins.dict
 |      builtins.object
 |
 |  Methods defined here:
 |
 |  __delitem__(self, key, /)
 |      Delete self[key].
 |
 |  __eq__(self, value, /)
 |      Return self==value.
 |
 |  __ge__(self, value, /)
 |      Return self>=value.
 |
 |  __gt__(self, value, /)
 |      Return self>value.
 |
 |  __init__(self, /, *args, **kwargs)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |
 |  __iter__(self, /)
 |      Implement iter(self).
 |
 |  __le__(self, value, /)
 |      Return self<=value.
 |
 |  __lt__(self, value, /)
 |      Return self<value.
 |
 |  __ne__(self, value, /)
 |      Return self!=value.
 |
 |  __reduce__(...)
 |      Return state information for pickling
 |
 |  __repr__(self, /)
 |      Return repr(self).
 |
 |  __reversed__(...)
 |      od.__reversed__() <==> reversed(od)
 |
 |  __setitem__(self, key, value, /)
 |      Set self[key] to value.
 |
 |  __sizeof__(...)
 |      D.__sizeof__() -> size of D in memory, in bytes
 |
 |  clear(...)
 |      od.clear() -> None.  Remove all items from od.
 |
 |  copy(...)
 |      od.copy() -> a shallow copy of od
 |
 |  items(...)
 |      D.items() -> a set-like object providing a view on D's items
 |
 |  keys(...)
 |      D.keys() -> a set-like object providing a view on D's keys
 |
 |  move_to_end(self, /, key, last=True)
 |      Move an existing element to the end (or beginning if last is false).
 |
 |      Raise KeyError if the element does not exist.
 |
 |  pop(...)
 |      od.pop(k[,d]) -> v, remove specified key and return the corresponding
 |      value.  If key is not found, d is returned if given, otherwise KeyError
 |      is raised.
 |
 |  popitem(self, /, last=True)
 |      Remove and return a (key, value) pair from the dictionary.
 |
 |      Pairs are returned in LIFO order if last is true or FIFO order if false.
 |
 |  setdefault(self, /, key, default=None)
 |      Insert key with a value of default if key is not in the dictionary.
 |
 |      Return the value for key if key is in the dictionary, else default.
 |
 |  update(...)
 |      D.update([E, ]**F) -> None.  Update D from dict/iterable E and F.
 |      If E is present and has a .keys() method, then does:  for k in E: D[k] = E[k]
 |      If E is present and lacks a .keys() method, then does:  for k, v in E: D[k] = v
 |      In either case, this is followed by: for k in F:  D[k] = F[k]
 |
 |  values(...)
 |      D.values() -> an object providing a view on D's values
 |
 |  ----------------------------------------------------------------------
 |  Class methods defined here:
 |
 |  fromkeys(iterable, value=None) from builtins.type
 |      Create a new ordered dictionary with keys from iterable and values set to value.
 |
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |
 |  __dict__
 |
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |
 |  __hash__ = None
 |
 |  ----------------------------------------------------------------------
 |  Methods inherited from builtins.dict:
 |
 |  __contains__(self, key, /)
 |      True if the dictionary has the specified key, else False.
 |
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |
 |  __getitem__(...)
 |      x.__getitem__(y) <==> x[y]
 |
 |  __len__(self, /)
 |      Return len(self).
 |
 |  get(self, key, default=None, /)
 |      Return the value for key if key is in the dictionary, else default.
 |
 |  ----------------------------------------------------------------------
 |  Static methods inherited from builtins.dict:
 |
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.

"""




