"""
TIPO BOOLEAMO

AlGEBRA BOLEANO -> Criada por Geoge Boole

TEMOS 2 CONSTANTES, Verdadeiro ou Falso

True -> Verdadeiro
False -> Falso

ps: Sempre com a inicial Maiúscula

Geralmente usamos o booleano para operações basicas.
"""

ativo = False

print(ativo)

"""
Operações Basicas:
"""

# NEGAÇÃO (NOT)
"""
FAZENDO A NEGAÇÃO, SE O VALOR BOOLEANO FOR VERDADEIRO SERÁ FALSO,
SE O RESULTADO FOR FALSO SERA VERDADEIRO OU SEJA SEMPRE O CONTRARIO
"""
print(not ativo)

# OU (OR)
"""
É UMA OPERAÇÃO BINÁRIA, OU SEJA, DEPENDE DE 2 VALORES. OU UM OU OUTRO DEVE SER VERDADEIRO.

True or True = True
True or False = True
False or True = True
False or False = False
"""

logado1 = False
logado2 = False
print(logado1 or logado2)

# E (AND)
"""
TAMBEM É UMA OPERAÇÃO BINARIA, OU SEJA, DEPENDE DE 2 VALORES. AMBOS OS VALORES DEVEK SER VERDADEIRO

True and True = True
True and False = False
False and True = False
False and False = False
"""

logado3 = True
logado4 = False

print(logado3 and logado4)

"""
TAMBEM TEMOS AS COMPARAÇÕES ENTRE VARIAIS E NUMEROS QUE NEM TODA LINGUAGEM DE PROGRAMAÇÃO
"""


print(dir(True))