"""
Geradores [Generators] sao iteraveis.

ps. O contrario nao é verdadeiro. [Ou seja, nem todo Iterator é um Generetor.

Outras informacoes:

    > Generetors podem ser criados com funcoes geradoras.
    > Funcoes geradoras, utiliozam a palabra reservada `yield`
    > Generetors podem ser criados com Expressoes geradoras.

Diferenca entre Funcoes e Generators Fuction :

------------------------------------------------------------------------------------------------
                Function             |                       Generator Function
------------------------------------------------------------------------------------------------
    >Utilizam a palavra return      |                  > Utilizam a palavra yield *Principal diferenca
------------------------------------------------------------------------------------------------
    >Retorna uma vez                |                  > Pode utilizar yield multiplas vezes
------------------------------------------------------------------------------------------------
    >Pode retornar um valor         |                  > Retorna um Generator
________________________________________________________________________________________________
"""

#Exemplo Generator function

def count(max_value):
    count_control = 1
    while count_control < max_value:
        yield count_control          #para aqui esperando a funcao next
        count_control += 1

#OBS: uma generator function náo é um Generator, ele ira gerar um Generator.


it = count(100)

print(type(it))

print(next(it))

for n in it:
    print(n)