"""
Debuggando com PDB

Vida de Inseto -> Life`s bug

Bug -> inseto

# OBS: A utilizacao do print() para debugar codigo e uma pratica ruim.
def dividir(a, b):
    print(f'a = {a} e b={b}')
    try:
        return int(a) / int(b)
    except(ValueError, ZeroDivisionError) as err:
        return f'Ocorre um problema {err}'

print(dividir(4,7))

# Existem formas mais profissionais de se fazer esse `debug`, utilizando o debugger
# Em Python, podemos fazer isso em diferentes IDEs, como o PyCharm ou utilizando
# O PDB - Python Debugger

def dividir(a, b):
    try:
        return int(a) / int(b)
    except(ValueError, ZeroDivisionError) as err:
        return f'Ocorre um problema {err}'

print(dividir(4,0))

#  Exemplo com PDB - Python Debugger

# Para utilizar o Python Debugger, precisamos* (Python < 3.7) importar a biblioteca pdb e entao
# utilizar a funcao set_trace()

# Comandos basicos do PDB
# l (listar onde estamos no codigo)
# n (proxima linha)
# p (imprime variavel)
# c (continua a execucao - finaliza o debugging)

nome = 'Angelina'
sobrenome = 'Jolie'
import pdb; pdb.set_trace()
nome_completo = nome + ' ' + sobrenome
curso = 'Programacao Em Python'
final = nome_completo + 'faz o curso' + curso
print(final)

# Porque utilziar este formato formato?
# O debug e utilizado durante o desenvolvimento. Custumamos realizar os imports de
# bibliotecas no inicio do arquivo. Por isso ao inves de colocarmos o import do pdb
# nos colocamos somente onde vamos debuggar, e ao finalizar ja fazemos a remocao.

# A partir do Python 3.7, nao e mais necessario importar a biblioteca pdb, pois o comando
# de debug foi incorporado como funcao built-in (integrada) chamada breakpoint()

nome = 'Angelina'
sobrenome = 'Jolie'
breakpoint()
nome_completo = nome + ' ' + sobrenome
curso = 'Programacao Em Python'
final = nome_completo + 'faz o curso' + curso
print(final)

# OBS: Cuidado com conflitos entre nomes de variaveis e os comandos do pdb

"""


