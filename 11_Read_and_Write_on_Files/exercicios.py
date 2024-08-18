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

<<<<<<<



"""

import os
"""

#MANEIRA 1
letters_count: int = 0
with open('new_file', 'r') as file:
    lines = file.readlines()
    for line in lines:
        for letter in line:
            if letter == '\n':
                letters_count += 1
            elif letter == ' ':
                letters_count += 1

print(f'{letters_count}')
"""

#MANEIRA 2
file : str = input('Informe qual arquivo deseja abrir:')
with open(file, 'r') as file_read:
    lines = file_read.readlines()

print(f'The file has {len(lines)} lines')