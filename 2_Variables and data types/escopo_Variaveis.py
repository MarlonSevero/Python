"""
Escopo de Variaveis

Dois casos de Escopo

1 - Variaveis Globais
    -Variaveis globais são reconhecidas, ou seja, seu escopo compreende , todo o programa.

2 - Variaveis Locais
    -Variaveis locais são reconhecidas somente no bloco onde foram declaradas, ou seja, seu escopo
    está limitado ao bloco onde foi declarada

Para declarar variaveis em Python fazemos:

nome_da_variavel = valor_da_variavel

Python é uma linguagem de tipagem dinâmica, isso significa que
ao declararmos uma variável, nós não colocamos o tipo de dado dela.
Este tipo é inferido ao atribuirmos o valor a mesma.

Python
num = 42 *Python sabe que é inteiro
"""

n = 50 #Variavel Global

print(n)

if(n > 10):
    novo = n + 10 #A variavel esta declarada localmente dentro do Bloco IF por tanto é local
    print(novo)

print(novo) #só vai imprimir o valor se entrar na condição, se não a variavel não é criada
