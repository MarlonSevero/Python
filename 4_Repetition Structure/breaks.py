"""
Saindo de loops com break

Funciona da mesma forma que nas linguagens C ou Java:

Ultilizamos o break para sair de loops de maneira projetada.
"""

#Exemplo 1

for n in range(1, 11):
    if n == 6:
        break
    else:
        print(n)

print('Sai do Loop')

# Exemplo 2

while True:
    comando = input("Digite 'sair' para sair:")
    if comando == 'sair':
        break

