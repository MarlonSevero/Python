"""
Recebendo dados do usuario

input() -> Todo dado recebido via input é do tipo String

Em pytho, String é tudo que estiver entre:

- Aspas simples;
- Aspas duplas;
- Aspas simples triplas;
- Aspas duplas triplas;

Exemplos:

- Aspas simples -> 'angelina Jolie'
- Aspas duplas -> "angelina Jolie"
- Aspas simples -> '''angelina Jolie'''
"""
# Aspas duplas triplas -> """angelina Jolie"""
# Entrada de Dados
#print("what's your  name?")


"""
name = input()  # input -> Entrada de dados

O input é um recurso integrado do Python, 
no qual faz parte das *builtins*
Built-in Objects (Objetos Integrados)

"""

name = input("what's your  name?")


# EXEMPLO DE PRINT 'ANTIGO 2.X'
# print('Seja Bem-vindo(a) %s' % name)

# EXEMPLO DE PRINT 'MAIS ATUAL' 3.7
print(f'Seja bem-vindo(a) {name}')

# print("Qual sua idade?")
# idade = input()
idade = int(input('Qual sua idade?'))

# Processamento
# Saída de dados
# print('A %s tem %s anos' % (name, idade))

# EXEMPLO DE PRINT 'MODERNO' 3.x
# print('Seja Bem-Vindo(a){0}'.format(name))
# print('A {0} tem {1} anos' .format(name, idade))

# EXEMPLO DE PRINT 'MAIS ATUAL' 3.7
print(f'A {name} tem {idade} anos')
print(f'Meu nome é {name}')
"""
# int(idade) => cast
Cast é a 'conversão' de um tipo de dado para outro
"""


print(f'Ola {name} voce nasceu em {2024-int(idade)}')
