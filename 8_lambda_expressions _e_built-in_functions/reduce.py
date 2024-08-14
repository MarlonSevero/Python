"""
Reduce

OBS: A partir do PYTHON 3.x o função reduce() não é mais uma função integrada (built-in)
Agora temos que importar e utilizar esta função a partir do modulo 'functools'

Guido : 'Utilize a função reduce() se voce realmente precisa dela. Em todo caso
99% das vezes um loop for é mais legível.

Para entender o reduce():

# Imagine que voce tem uma colecao de dados:

dados = [a1, a2, a3, ..., an]

# E voce tem uma funcao que recebe dois parametros (diferente de map e filter que recebe apenas 1):

def funcao(x, y):
    return x + y

Assim como map() e filter(), a funcao reduce() recebe dois parametros: a funcao e o iteravel.

reduce(funcao, dados)

A funcao reduce(), funciona da seguinte forma:

    * Passo1: res1 = f(a1, a2) # Aplica a funcao nos dois primeiros elementos da colecao e guarda o resultado.
    * Passo2: res2 = f(res1, a3) # Aplica a funcao passando o resultado do passo1 mais o terceiro elemento
    e guarda o res.

    Isso e repetido ate o final.

    * Passo 3: res3 = f(res2, a4)
    .
    .
    .
    * Passo n: resN = f(resM, aN)

Ou seja, em cada passo ela aplica a funcao passando como primeiro argumento o resultado da aplicacao anterior.
No final, reduce() ira retornar o resultado final.

Alternativamente, poderiamos ver a funcao reduce() como:

Funcao(funcao(funcao(a1, a2), a3), a4), ...), aN)

# Como funciona na pratica?

# Vamos utilizar a funcao reduce() para multiplicar todos os numeros de uma lista

from functools import reduce

dados = [1, 2, 3, 4, 5, 6, 7, 8, 9]

multi = lambda x, y: x * y

res = reduce(multi, dados)
print(res)

# Utilizando um loop normal:

res = 1
for n in dados:
    res = res * n
print(res)

"""


