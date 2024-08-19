"""

Crie um programa que receba uma lista de idades e, usando if/else, classifique cada idade como
"Criança", "Adolescente", "Adulto" ou "Idoso".


def valida_idade(idades: dict):
    for key, value in (idades.items()):
        if value < 18:
            print(f'{key} tem {value} anos, logo é nao pode entrar')
        elif value == 18:
            print(f'{key} tem {value} anos,
            print(f'ok pode entrar {key} voce ja tem {value} anos')
    return valida_idade
 --------->>><<<<<--------
class Calculator:
    def __init__(self, num1: int, num2: int):
        self.num1 = num1
        self.num2 = num2

    def soma(self):
        return self.num1 + self.num2

calcu = Calculator(10, 10)

print(calcu.soma())



"""

"""
def aumentar(funcao):
    def loud(nome):
        return funcao(nome).upper()
    return loud

@aumentar
def saudacao(nome):
    return f'hello {nome}'
    
    
    def validaPositivo(verify_function):
    def verify(number):
        if number < 0:
            return f'{verify_function(number)} is negative'
        else:
            return f'{verify_function(number)} is positive'
    return verify

"""




def recursive(number):
    if number == 0 or number == 1:
        return 1
    else:
        return number * recursive(number - 1)
