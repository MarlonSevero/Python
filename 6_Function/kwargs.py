"""
**kwargs

kwargs - Dicionario

Poderiamos chamar esse parametro de **xis, mas por convção chamamos de duplo asterisco **kwargs

Esse é só mais um parâmetro, mas diferente do *args que coloca os valores extras em uma tupla,
o **kwargs exige que utilizemos parâmetros nomeados, e tranforma esses parâmetros extras em um dicionário.

# exeplo 1
def cores_favoritas(**kwargs):
    print(kwargs)

cores_favoritas(marcos ='Verde', Juliana='Azul', Fernanda='Amarelo',Vanessa='Branco')

# exeplo 2


def cores_favorit(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f"A cor favorita de {pessoa.title()} é {cor}")


cores_favorit(marcos ='Verde', Juliana='Azul', Fernanda='Amarelo',Vanessa='Branco')


# OBS: Os parâmetros *args e **kwargs não são obrigatórios.

cores_favorit()
cores_favorit(marlon='Verde')

# Exemplo 3

def compr_esp(**kwargs):
    if 'geek' in kwargs and kwargs['geek'] == 'Python':  # Verificando se eu tenho a chave 'Geek' dentro do dicionario
        return 'Você Recebeu um Comprimento Pythônico Geek'
    elif 'geek' in kwargs:
        return f"{kwargs['geek']} Geek!"
    return 'Não tenho certeza de quem você é....'


print(compr_esp())
print(compr_esp(geek='Python'))
print(compr_esp(geek='Oi'))
print(compr_esp(geek='Especial'))



******* ORDEM CORRETA DE DECLARAÇÃO DOS PARAMETROS *******

# Nas nossas funções, podemos ter (NESTA ORDEM) :

# Parâmetros Obrigatórios
# *Args;
# Parâmetros Default (Não Obrigatórios)
# **Kwargs

# Exemplo:


def minha_funcao(nome, idade, *args, solteiro=False, **kwargs):
    print(f'O {nome} tem {idade} anos')
    print(args)
    if solteiro:
        print('Solteiro ')
    else:
        print('Casado')
    print(kwargs)


minha_funcao(8, 'Julia')

# Obrigatorios: 8, Julia
# *Args = VAZIO
# Default = VAZIO
# **Kwargs = VAZIO

minha_funcao(18, 'João', 4, 5, 6, solteiro=True)

# Obrigatórios: 18, João,
# *Args = 4,5,6
# Default = True
# **Kwargs = VAZIO

minha_funcao(34, 'Felipe', eu='Não', voce='vai')

# Obrigatórios: 34, Felipe,
# *Args = VAZIO
# Default = VAZIO
# **Kwargs = # **Kwargs = {eu:Nao, voce:vai}

minha_funcao(19, 'Carla', 9, 4, 3, 'java' = 'False', 'python' = 'True')

# Obrigatórios: 19, Carla
# *Args = 9, 4, 3
# Default = VAZIO
# **Kwargs = {'java' : 'False', 'python' : 'True' }

****** Entenda porque é importante manter a ordem correta dos parâmetros na declaração.******

# Função com a ordem CORRETA de paramêtros

def mostra_info(a, b, *args, instrutor='Geek', **kwargs):
    return [a, b, args, instrutor, kwargs]

print(mostra_info(1, 2, 3, sobrenome='University', cargo = 'Instrutor'))

# Obrigatórios: 1, 2
# *Args = (3, )
# Default = VAZIO
# **Kwargs = {'sobrenome' : 'University', 'cargo' : 'Instrutor' }

# Função com a ordem INCORRETA de paramêtros


def mostra_info(a, b, instrutor='Geek', *args, **kwargs):
    return [a, b, args, instrutor, kwargs]


print(mostra_info(1, 2, 3, sobrenome='University', cargo = 'Instrutor'))

# Obrigatórios: 1, 2
# *Args = VAZIO
# Default = 3
# **Kwargs = {'sobrenome' : 'University', 'cargo' : 'Instrutor' }

*** Desempacotas com *Kwargs ***

def mostra_nome(**kwargs):
    return f"{kwargs['nome']} {kwargs['sobrenome']}"

nomes = {'nome': 'Marlon', 'sobrenome': 'Salles'}

print(mostra_nome(**nomes))

#  O duplo asperisco desempacota o dicionario

def soma_multiplos_numeros(a, b, c):
    print(a + b + c)

lista = [1, 2, 3]
tupla = (1, 2, 3)
set = {1, 2, 3}

soma_multiplos_numeros(*lista)
soma_multiplos_numeros(*tupla)
soma_multiplos_numeros(*set)

dicionario = dict(a=1, b=2, c=3)

soma_multiplos_numeros(**dicionario)

# OBS! Os nomes da chave de um dicionário devem ser os mesmos dos parâmetros da função.

# dicionario = dict(f=1, g=2, h=3) - TypeError
# soma_multiplos_numeros(**dicionario)

# Podemos passar com adicionais

def soma_multiplos_numeros(a, b, c, **kwargs):
    print(a + b + c, kwargs)

dicionario = dict(a=2, b=4, c=8,marlon='Salles' )

soma_multiplos_numeros(**dicionario)

"""

def cores_favoritas(**kwargs):
    print(kwargs)

cores_favoritas(marcos ='Verde', Juliana='Azul', Fernanda='Amarelo',Vanessa='Branco')





