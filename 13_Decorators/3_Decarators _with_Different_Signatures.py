"""
Decoradores com diferentes assinaturas


def aumentar(funcao):
    def loud(nome):
        return funcao(nome).upper()
    return loud

@aumentar
def saudacao(nome):
    return f'hello {nome}'

@aumentar
def pedir(principal, acompanhamentos):
    return f'seu pedido é {principal} e {acompanhamentos}'

print(saudacao('name'))
print(pedir('picach', 'batata frita'))

ps.Vai retornar erro

#Devem utilizar sempre o Decorator Patter para resolver

#Refatorando com Decarator Patter.

def aumentar(funcao):
    def loud(*args, **kwargs):
        return funcao(*args, **kwargs).upper()
    return loud

@aumentar
def saudacao(nome):
    return f'hello {nome}'

@aumentar
def pedir(principal, acompanhamentos):
    return f'seu pedido é {principal} e {acompanhamentos}'

print(saudacao('name'))
print(pedir('picanha', 'batata frita'))


#Refatorando com Decarator Patter.

def gritar(funcao):
    def loud(*args, **kwargs):
        return funcao(*args, **kwargs).upper()
    return loud

@gritar
def saudacao(nome):
    return f'hello {nome}'

@gritar
def pedir(principal, acompanhamentos):
    return f'seu pedido é {principal} e {acompanhamentos}'

print(saudacao('name'))
print(pedir('picanha', 'batata frita'))

#A assinatura de uma funcao é representada pelo seu retono, nome e parametros de entrada.


@gritar
def lol():
    return 'lol'

print(lol())
"""

#Decorators com parametros de entrada


def verify_first_argument(value):
    def return_verify(function_verify):
        def verify(*args, **kwargs):
            if args and args[0] != value:
                return f'Incorret Value, the first value must be {value}'
            return function_verify(*args, **kwargs)
        return verify
    return return_verify


@verify_first_argument('Pizza')
def favorite_foods(*args):
    return f'{args}'

@verify_first_argument(10)
def sum_ten(num1, num2):
    return num1 + num2

print(favorite_foods('Pizza', 'banana'))

print(sum_ten(10,  10))