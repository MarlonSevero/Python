"""

"for loop"

***Python***
for item in interavel
    //execução do Loop

Ultilizamos Loops para iterar sobre sequências ou sobre valores iterável

Exemplos de Iteraveis:

-String
    nome = "Geek University"

-Lista
    lista = [ 1, 3, 5, 7, 9 ]

-Range
    numeros = [1, 10]

    #exemplo de for 1 (Iterando em uma string)
for letra in nome:
    print(letra)

#exemplo de for 2 (Iterando em uma lista)
for n in lista:
    print(n)

#exemplo de for 3 (Iterando em um range)
for n in range(1, 10):
    print(n)

range(valor_inicial, valor_final)
obs: O valor final não é incluso.
1 ... 9, 10 -> Não
"""

"""
***Enumerate:***

nome = 'Geek University'
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10) # Temos que transforma em uma lista

for indice, letra in enumerate(nome):
    print(nome[indice])
    "NOME NA POSIÇÃO 0, DEPOIS, INDICE NA POSIÇÃO 1 E ASSIM POR DIANTE"
ou
    for _, v in enumerate(nome):
    print(nome[v])

***Obs: Quando não precisamos de um valor podemos descartalo ultilizando um underline (_)***
for _, letra(valor) in enumerate(nome):
    print(nome[letra])
    
***Exemplo do Enumerate***
for valor in enumerate(nome):
    print(valor)

(0, seq [0]), (1, seq [x]), (2, seq [y]...)
    
**O QUE REALMENTE O ENUMARATE TEM**    
for valor in enumerate(nome):
    print(valor)
    
    for valor in enumerate(nome):
    print(valor[0 OU 1])
   
***OUTRAS FORMA DE USO***

    qtd = int(input("Quantas vezes esse Loop deve rodas? "))
    for n in range(1, qtd + 1):
    print(f"Imprimindo {qtd} vezes")
    
    soma = 0
        for n in range(1, qtd + 1):
        num = int(input(f"Informe o ({n}/{qtd}) valor: "))
        soma = soma + num
    print(f"A soma é:{soma}")
   
   # Imprimindo sem pular linha 
   
    nome = "Marlon Salles"
    for letra in nome:
    print(letra, end='')
    
***CTROL + CLICK EM CIMA DA FUNÇÃO, ABRE A DOCUMENTAÇÃO DELA.
   FAZ A MESMA COISA DO QUE O HELPnPORÉM VAI DIRETO NO CODIGO***
 
 Podemos multiplicar string por inteiros 
 
 nome = "Marlon"
 nome * 3
 resultado = MarlonMarlonMarlon   
 
 
"""

"""


# https://apps.timwhitlock.info/emoji/tables/unicode
# ORIGINAL: U+1F61D
# + -> 000
# MODIFICADO:  U0001F61D

for _ in range(3):
    for num in range(1, 11):
        print('\U0001F621' * num)

nome = 'Geek University'
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10) # Temos que transforma em uma lista
"""
qtd = int(input("Quantas vezes esse Loop deve rodas? "))
soma = 0
for n in range(1, qtd + 1):
    num = int(input(f"Informe o ({n}/{qtd}) valor: "))
    soma = soma + num
print(f"A soma é:{soma}")
