"""
Para fazer uma de manipulacao de arquivos do sistema operacional.

Precisa realizar a importacao do modulo os (Operation System)

import os

print(os.getcwd()) # Retorna caminho absoluto. Current Work Directory

os.chdir('/') #Para mudar o diretorio. Change Directory

print(os.getcwd())

print(os.path.isabs('/Users/')) #True "Is absolute?
print(os.name) #Retorna se o sistema operacional é Windows(nt) e Posix (Linux, Mac)

print(os.uname()) # É exibido

import sys

print(sys.platform)

#/Users/teste/Desktop/workspace_temp
os.chdir('/Users/teste/Desktop/workspace_temp')
res = os.path.join(os.getcwd(), 'teste') # os.path.join(diretorio atual, diretorio que seja feito o join (criado)
print(res)

print(os.listdir('/etc/')) #Listando os diretorios
print(os.listdir()) #listando no atual
print(os.scandir('/etc')) #scandir temos uma listagem com mais informacao
print(list(os.scandir())) #transformando o scan em uma lista

files = list(os.scandir('/etc'))
print(files)
print(files[0].name) #Nome do Arquivo)
print(files[0].is_dir()) #Bool is a directory
print(files[0].is_symlink()) #bool is a symbolic link
print(files[0].inode()) #id on the path
print(files[0].path) #file path
print(files[0].stat()) #Estatisticas sobre o arquivo





"""

import os

scan_files = os.scandir('/etc')
files = list(scan_files)

print(files)
print(files[0].name) #Nome do Arquivo)
print(files[0].is_dir()) #Bool is a directory
print(files[0].is_symlink()) #bool is a symbolic link
print(files[0].inode()) #id on the path
print(files[0].path) #file path
print(files[0].stat()) #Estatisticas sobre o arquivo

scan_files #O ideal é a gente sempre fechar o `scandir`




