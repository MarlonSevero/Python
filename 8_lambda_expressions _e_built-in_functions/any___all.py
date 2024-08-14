"""
Any e All

All () -> Retorna True se todos os elementos do iteravel sao verdadeiros ou ainda se o iteravel
esta vazio.

# Exemplos all() :

print(all([0, 1, 2, 3, 4, 5])) # Todos os elementos da lista sao veradedeiros ? False

print(all([1, 2, 3, 4, 5])) # Todos os elementos da lista sao veradedeiros ? True

print(all([])) #True

print(all((1, 2, 3, 4, 5))) #True

print(all({1, 2, 3, 4, 5})) #True

print(all('Geek')) #True

# Poderiamos usar de uma maneira diferente:

# Exemplo:

nomes = ['Camila', 'Carlos', 'Carla']
print(all([nome[0] == 'C' for nome in nomes]))

obs: Um interavel vazio convertido para bool e False mas o all() considera como True

print(all([num for num in [11, 13, 7, 7, 21] if num % 2 == 0]))

Any -> Retorna True se qualquer elemento do iteravel for verdadeiro. Se o iteravel estiver vazio,
retorna False.

print(any([0, 1, 2, 3, 4, 5])) # True
print(any([0, (), {}, []])) # False

nomes = ['Camila', 'Carlos', 'Carla', 'Vanessa']
print(any([nome[0] == 'C' for nome in nomes]))

pri                          nt(any([num for num in [11, 13, 7, 7, 21] if num % 2 == 0]))

"""

both = []
numbers = [1, 2, 3, 4, 5]
letters = ['a', 'b', 'c', 'd', 'e']


for i in numbers:
    for j in letters:
        print(f"{i}/{j}")
        both.append()