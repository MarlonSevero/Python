"""
Mapas -> Conhecidos em Python como Dicionarios

Dicionarios em Python sao representados por chaves {}

# ps: complemento da aula de dicionarios

# Iterando sobre dicionarios

receita = {'jan': 100, 'fev': 200, 'mar': 300}

for chave in receita:
    print(chave)
ou podemos fazer tambem:
for chave in receita:
    print(receita[chave])
e até mesmo assim:
for chave in receita:
    print(f'Em {chave} recebi R$: {receita[chave]}')

*** POREM O JEITO CERTO SEGUE ABAIXO ***

# Jeito pythonico de fazer
# Esse metodo nos tras um dicionario de chaves
print(receita.keys())

print(receita)

for chave in receita.keys():
    print(receita[chave])

** # Acessando as chaves **

print(receita.keys())

for chave in receita.keys():
    print(receita[chave])

** # Acessando os valores **
# Cria um dicionario de valores

print(receita.values())

for valor in receita.values():
    print(valor)

print(receita)

** # Desempacotamento de dicionarios **

print(receita.items())
# Cria um dicionario de itens
# Contem lista contendo tuplas do tipo (chave, valor)

# Soma*, valor Mãximo*, Valor Minimo*, Tamanho

# * Se os valores forem todos inteiros e reais

print(sum(receita.values()))
print(max(receita.values()))
print(min(receita.values()))
print(len(receita))
"""
