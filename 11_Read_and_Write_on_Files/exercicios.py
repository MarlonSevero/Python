"""

a) Crie/abra um arquivo texto de nome “arq.txt”
b) Permita que o usuário grave diversos caracteres nesse arquivo, até que o usuário entre com o caractere
“0”.
c) Feche o arquivo
d) Abra, leia o arquivo e escreva na tela todos os caracteres armazenados

with open('new_file', 'a') as file:
    while True:
        temp_word: str = str(input('What do you want write or 0 to exit:'))
        if temp_word != '0':
            file.write(temp_word)
        else:
            break

with open('new_file', 'r') as file:
    words = file.read()

for word in words:
    print(word)

<<<<<

"""

import os

vogais = []
concoantes = []

with open('new_file', 'r') as file:
    words = list(file)
    for word in words:
        for letter in word:
            if letter in ['a', 'e', 'i', 'o', 'u']:
                vogais.append(letter)
            elif letter != ' ':
                concoantes.append(letter)
print(f'Existe {len(vogais)} vogais no arquivo')
print(f'Existe {len(concoantes)} concocantes no arquivo')
