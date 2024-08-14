"""
Listas Aninhadas (Nested Lists)

- Algumas linguagens de programação (C+/JAVA) possuem uma entrutura de dados chamadas de arrays.
    - Unidimencionais (Arrays/Vetores)
    - Multidimencionais (Matrizes)

Em Python nos temos as Listas:

numeros = [1, 2, 'a', True, 3.14]

# Exemplos:

listas= [[1, 2, 3], [4, 5, 6], [7, 8, 9]] # Chamado de Matrizes em outras linguagens (3x3)
print(listas)
print(type(listas))

# Como fazer para acessar os dados?

print(listas[0])
print(listas[0][1]) # Linha Zero Coluna 1
print(listas[2][1])

# Iterando com Loops em uma lista aninhada.
for lista in listas:
    for num in lista:
        print(num)


# List Comprehension

[[print(valor) for valor in lista] for lista in listas]

# Para cada lista dentro das listas
pegue esse valor dentro da lista e exiba na tela.
1° Parte - for lista in listas
2° Parte - print(valor) for valor in lista

# Outros Exemplo

# Gerando um tabuleiro/matriz 3x3

tabuleiro = [[numero for numero in range(1, 4)]for valor in range(1, 4)]
print(tabuleiro)

# Colunas: for valor in range(1, 4)
# Linhas: numero for numero in range(1, 4)

# Gerando jogadas para o jogo da velha

velha = [['X' if numero % 2 == 0 else 'O' for numero in range(1, 4)] for valor in range(1, 4)]
print(velha)

# Gerando valores Iniciais
jogadas = [['anything' for numero in range(1, 4)] for valor in range(1, 4)]
print(jogadas[0][0])

"""

#numeros = [[numero * 100 for numero in range(0, 10)] for numero in range(1, 6)]
#print(numeros)

aulas = ['Programação', 'Banco de Dados', 'Analise de Projetos', 'Calculo I', 'Calculo II']

classes = [[f'Professor Faltou em {aula}' if aula == 'Calculo I' else 'Hoje tem essa aula de ' + aula for aula in aulas]for aula in range(2)]
print(classes)

j = [10, 11, 13, 17, 20, 30]

#ij = [[(f'{i} Meu Pau') for i in j] for i in j]

ij = 0
for i in j:
    for i in j:
        print(ij)