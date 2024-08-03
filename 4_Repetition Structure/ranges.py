"""
Ranges

- Precisamos conhecer o Loop For para usar os ranges
- Precisamos conhecer o Range para Trabalhar melhor com Loops For

Ranges são ultilizados para gerar sequências numericas, não de forma aleatória
mas sim de maneira especificada.

Formas Geral:

#Forma 1

range(valor_de_parada)

OBS: valor_de_parada não incluso (inicio padrão 0, e passo de 1 em 1)
# Exemplo Forma 1
for num in range(11):
    print(num)

#Forma 2

range(valor_de_inicio, valor_de_parada)

OBS: valor_de_parada não incluso (inicio especificado pelo usuario, e passo de 1 em 1)
# Exemplo Forma 2
for num in range(4, 11):
    print(num)

#Forma 3
range(valor_de_inicio, valor_de_parada, passo)BR

OBS: valor_de_parada não incluso (inicio especificado pelo usuario, e passo especificado pelo usuario)
# Exemplo forma 3
for num in range(5,50,5):
    print(num)

#Forma 4 (Inversa)
range(valor_inicio, valor_de_parada, passo)
OBS: valor_de_parada não incluso (inicio especificado pelo usuario, e passo especificado pelo usuario)

# Exemplo forma 4

for num in range(10, -100, -10):
    print(num)

#Fazendo um lista com Ranges, estamos convertendo um range em uma lista
lista = list(range(10))
"""

for num in range(50):
    print("RANGES SÃO O FUTURO DA PROGRAMAÇÃO")
