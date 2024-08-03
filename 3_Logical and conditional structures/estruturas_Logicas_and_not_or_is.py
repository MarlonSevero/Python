"""
Estruturas Logicas: and (e), not (nao), or (ou), is (é)

Operadores Unários:
    -not, is
Operadores Binários:
    -And, Or

Regras de Funcionamento:
    -Para o 'AND' ambos os valores precisam ser True
    -Para o 'OR' um ou outro valor precisa ser True
    -Para o 'NOT' o valor booleano é invertido, ou seja, True vira False e False vira True
    -Para o 'IS' o valor é comparado com um segundo
"""

ativo = True
logado = False

#Se não estiver ativo
if not ativo:
    print("Ative sua Conta.")
else:
    print("Bem-Vindo.")

#print(not False)

#Ativo é Falso?
print(ativo is False)

