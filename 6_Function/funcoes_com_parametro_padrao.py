"""
Funções com Parâmetro Padrão (Default Paramters)

- Funções onde a passagem de parâmetro seja opcional;

# Exemplo de função onde a passagem de parametro seja opcional
print('Geek')

print()

# Exemplo de função onde a passagem de parêmetro seja obrigatória:
def quadrado(numero):
    return numero**2


print(quadrado(4))
print(quadrado()) # TypeError


****** DEIXANDO UMA PARAMETRO OPCIONAL********


def exp(numero, potencia=2):
    return numero ** potencia


print(exp(2, 3))
print(exp(3, 2))

print(exp(3))   # Por padrão eleve ao quadrado
print(exp(3, 5))    # Eleva a potência informada pelo usuário

# OBS:
# Se o usuário passar somente 1 argumento, este será atribuído ao parametro 'numero', e será calculado o quadrado desse número:
# Se o usuário passar 2 argumentos, o primerio sera atribuido 'numero' e o segundo ao parâmetro 'potencia'. Então
# será calculada esta potência.

**************


# obs: Em funções Python, os parâmetros com valores default (Padrão) DEVEM sempre estar ao final da declaração.

# ERRO!
def teste(potencia, num=2):
    return num**potencia

print(teste(6))

********** # Exemplo mais complexo: **************


def mostra_informacao(nome='Geek', instrutor=False):
    if nome == 'Geek' and instrutor:
        return 'Welcome Instrutor Geek!'
    elif nome == 'Geek':
        return 'Eu pensei que vc era o instrutor'
    return f'Olá, {nome}'


print(mostra_informacao())
print(mostra_informacao(instrutor=True))
print(mostra_informacao(True)) # ERRADO
print('Ozzy')
print(mostra_informacao(nome='Marlon'))

*******# Por que utilizar parâmetros com valor default ?********

- Nos permite ser mais flexível nas funções;
- Evita erros com parâmetros incorretos;
- Nos permite trabalhar com exemplos mais legível de código;

# Quais tipos de dados podemos utilizar como valores default para paâmetros?

- Qualquer tipo de dado:
    - Números, string, floats, booleanos, listas, tuplas, dicionários, funções e etc;


********* # Exemplos ************

def soma(num1, num2):
    return num1 + num2


def mat(num1, num2, fun=soma):
    return fun(num1, num2)


def sub(num1, num2):
    return num1 - num2


print(mat(2, 3))
print(mat(2, 2, sub))

# Podemos ter funções que são declaradas dentro de funções, e tambem tem uma forma especial de escopo de variável.

def fora():
    contador = 0

    def dentro():
        nonlocal contador
        contador = contador + 1
        return contador
    return dentro()

print(fora())
print(fora())
print(fora())

print(dentro()) #NameError


"""






