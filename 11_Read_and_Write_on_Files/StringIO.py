"""
StringIO

Para ler ou escrever dados em arquivos do sistema operacional. O software precisa ter permissao. Read/Write

StringIO -> Utilizado para ler e criar arquivos em memoria (nao grava em disco)
\

"""

from io import StringIO

mensagem = "Some Message\n"

#Criando o arquivo em memoria
arquivo = StringIO(mensagem)
#igual a arquivo = open('arquivo.txt', 'w')

#Lendo o arquivo
print(arquivo.read())

#escrevendo arquivo
arquivo.write("Another text\n")

#movimento o cursor
arquivo.seek(0)

print(arquivo.read())
