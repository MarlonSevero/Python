"""
TIPO STRING

Em Python, um dado é considerado do tipo string sempre que:

-Estiver entre aspas simples -> 'Uma String', 'a', '123','True'
-Estiver entre aspas duplas -> "Uma String", "a", "123","True"
-Estiver entre aspas simples triplas -> '''Uma String''', '''a''', '''123''','''True'''

\n -> Pula linha
"""
#-Estiver entre aspas duplas triplas -> """Uma String""", """a""", """123"""","""True"""

nome = "MARLON"
print(nome)
print(type(nome))

nome2 = "Marlon Salles\nSevero"
print(nome2.upper())
print(nome.lower())

# transforma numa lista de String
nome_lista = "Marlon Salles"
print(nome_lista.split())


nome3 = "Geek University"
print(nome3)

nome5 = "Marlon Salles"
print(nome5[0:4]) # slice de string

print(nome3[13])

# Começa no primeiro elemento, vá até o ultimo elemento e inverta

print(nome[:: -1]) # Inversão da String pythonico
nome4 = "Marlon Salles"
print(nome4 . replace("M","N"))




