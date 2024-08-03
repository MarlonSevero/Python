"""
Modulo Collections - Default Dict

# Recap Dicionários

dicionario = {'curso':'Python'}

print(dicionario)

print(dicionario['curso'])

print(dicionario['outro']) # ??? KeyError

Default Dict -> Ao criar um dicionário utilizando-o, nós informamos um valor default.
Podendo utilizar um lambda para isso. Este valor será utilizado sempre que não houver
um valor definido. Caso tentarmos acessar uma chave que não existe, essa chave será criada
e o valor default será atribuido.

OBS: Lambidas são funções sem nome, que podem ou nao receber valor de entrada e
retornar valores.


# Todas as funções dos dicionarios comuns funcionam aqui tambem

# Fazendo import

from collections import defaultdict

dicionario = defaultdict(lambda: 0)

dicionario['curso'] = 'Programação em Python: Necessario'

print(dicionario)

print(dicionario['outro']) # KeyError no dicionario comum, mas aqui não.

print(dicionario)



 ALL DOCUMENTATION DEFAULT DICT

**** help(defaultdict) ****

help(defaultdict)
Help on class defaultdict in module collections:

class defaultdict(builtins.dict)
 |  defaultdict(default_factory[, ...]) --> dict with default factory
 |
 |  The default factory is called without arguments to produce
 |  a new value when a key is not present, in __getitem__ only.
 |  A defaultdict compares equal to a dict with the same items.
 |  All remaining arguments are treated the same as if they were
 |  passed to the dict constructor, including keyword arguments.
 |
 |  Method resolution order:
 |      defaultdict
 |      builtins.dict
 |      builtins.object
 |
 |  Methods defined here:
 |
 |  __copy__(...)
 |      D.copy() -> a shallow copy of D.
 |
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |
 |  __init__(self, /, *args, **kwargs)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |
 |  __missing__(...)
 |      __missing__(key) # Called by __getitem__ for missing key; pseudo-code:
 |      if self.default_factory is None: raise KeyError((key,))
 |      self[key] = value = self.default_factory()
 |      return value
 |
 |  __reduce__(...)
 |      Return state information for pickling.
 |
 |  __repr__(self, /)
 |      Return repr(self).
 |
 |  copy(...)
 |      D.copy() -> a shallow copy of D.
 |
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |
 |  default_factory
 |      Factory for default value called by __missing__().
 |
 |  ----------------------------------------------------------------------
 |  Methods inherited from builtins.dict:
 |
 |  __contains__(self, key, /)
 |      True if the dictionary has the specified key, else False.
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
 |  Class methods inherited from builtins.dict:
 |
 |  fromkeys(iterable, value=None, /) from builtins.type
 |      Create a new dictionary with keys from iterable and values set to value.
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
