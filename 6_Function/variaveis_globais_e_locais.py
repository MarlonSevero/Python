"""
# Escopo - Evitar Problemas e confusões...

# Variáveis Globais

# Variáveis locais

Exemplos:

instrutor = 'Geek' # Variável Global

def diz_oi():
    instrutor = 'Python'    # Variável local
    return f'Olá {instrutor}'

print(diz_oi())

#OBS: Se tivermos uma variável local com o mesmo nome de uma variável global, a local terá preferência.

def diz_oi():
    prof ='Geek' # Variável Local
    return f'Olá {prof}'

print(diz_oi())
print(prof) #NameError

def diz_oi():
    prof ='Geek' # Variável Local
    return f'Olá {prof}'

print(diz_oi())
print(prof) #NameError

# ATENÇÃO com variáveis globais (Se puder evitar, evite!)

total = 0

def incrementa():
    total = total + 1   # UnboundLocalError (A variável local está sendo utilizada para processamento sem ter sido inicializada)
    return total

print(incrementa())

**** MANEIRA CERTA DE FAZER A UTILIZAÇÃO DA VARIAVEL GLOBAL NA FUNÇÃO ****

total = 0

def incrementa():
    global total    #Avisando que queremos utilizar a variável global
    total = total + 1
    return total

print(incrementa())
print(incrementa())
print(incrementa())

"""

