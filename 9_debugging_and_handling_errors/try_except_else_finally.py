"""
                    ** Try / Except / Else / Finally **

Dica de quando e onde tratar código:

TODA ENTRADA DE VE SER TRATADA!

OBS: A função do usuário é DESTRUIR seu sistema.


                            ** Else **

-> É executado somente se não ocorrer o erro.

try:
    num = int(input('Informe um numero:'))
except ValueError:
    print('Valor invalido')
else:
    print(f'O valor digitado é {num}')


                           **# Finaly **

try:
    num = int(input('Informe um numero:'))
except ValueError:
    print('Valor invalido')
else:
    print(f'O valor digitado é {num}')
finally:
    print('Sempre sou executado')

# O bloco finaly é SEMPRE executado. Independente se houver exceção ou não.

# O finaly, geralmente, é utilizado para fechar ou desalocar recursos


                    ** # Exemplo mais complexo ERRADO **

def dividir(a, b):
    return a / b

num1 = int(input('Informe o primeiro numero:'))
try:
    num2 = int(input('Informe o segundo numero:'))
except ValueError:
    print('O valor precisa ser numérico')
try:
    print(dividir(num1, num2))
except NameError:
    print('Valor incorreto')


                ** # Exemplo mais complexo CORRETO **

# OBS: Você é responsavel pelas entradas das suas funções. Então trate-as!

def dividir(a, b):
    try:
        return int(a) / int(b)
    except ValueError:
        return 'Valor Invalido'
    except ZeroDivisionError:
        return 'Não é possivel dividir por zero'

num1 = input('Informe o primeiro numero:')
num2 = input('Informe o segundo numero:')

print(dividir(num1,num2))


                    ** # Exemplo mais complexo - Genérico **

def dividir(a, b):
    try:
        return int(a) / int(b)
    except:
        return 'Ocorreu um problema '

num1 = input('Informe o primeiro numero:')
num2 = input('Informe o segundo numero:')

print(dividir(num1,num2))


                ** # Exemplo mais complexo - Semi-Genérico **

def dividir(a, b):
    try:
        return int(a) / int(b)
    except (ZeroDivisionError, ValueError) as err:
        return f'Ocorreu um problema {err}'

num1 = input('Informe o primeiro numero:')
num2 = input('Informe o segundo numero:')

print(dividir(num1,num2))


"""












