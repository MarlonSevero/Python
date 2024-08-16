"""
print(os.path.exists('random_file.txt')) #fazendo verificacao se um arquivo existe
print(os.path.exists('some_path'))  #fazendo verificacao se um diretorio existe.

#Criando arquivos

#Metodo 1 - Nao ideal
with open('new_file', 'w') as file:
    pass

#metodo 2 - Nao ideal
open('new_file', 'w').close()

#metodo 3 - ideal
os.mknod('new_file', 777) #MacOs ErrorPermition

#Criando Diretorios
os.mkdir('/etc/new/newPath') #MacOs ErrorPermition, #Somente newPath criado
os.makedirs('/etc/new/directory') #arvore de diretorios (mais de um) # Etc, new, direcotory criados
os.makedirs('/etc/new/', exist_ok=False)
os.rename('StringIO.py', 'NewStringIO') #Renomear pasta/diretorio, precisa estar vazio
os.rename('/etc/new/teste.txt', '/etc/newPath/teste.txt') #Renomeando arquivo
os.remove('file.txt') #utilizado para remover arquivo.
os.rmdir('random_path/another/one') # utilizado para remover diretorios [vazios]

#removendo uma arvore de arquivos

for file in os.scandir('path'):
    if file.is_file():
        os.remove(file.path)


3



"""
import os.path
import tempfile


# Arquivos temporarios

#Criando um diretorio temporario
with tempfile.TemporaryDirectory() as tmp:
    print('Criei um diretorio temporario')
    with open(os.path.join(tmp, 'temp_file.txt'), 'w') as temp_p:
        temp_p.write('Hello World')
        print(f'escrevi em {temp_p.name}')
        input()

#Criando um arquivo temporario.

with tempfile.TemporaryFile() as temp_file:
    temp_file.write(b'Hello World') #Em arquivos temporarios, so conseguimos escrever em Bytes. Por isso utilizamos 'b'


