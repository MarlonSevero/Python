
"""
2. Modos de Abertura de Arquivos
'r': Leitura (modo padrão). O arquivo deve existir.
'w': Escrita. Cria um novo arquivo ou sobrescreve o existente.
'a': Acrescentar. Adiciona ao final do arquivo, criando-o se não existir.
'b': Binário. Usado junto com outros modos, como 'rb' ou 'wb'.
'x': Exclusivo. Cria um novo arquivo e falha se o arquivo já existir.

3. Leitura de Arquivos
Para ler o conteúdo de um arquivo, você pode usar vários métodos:

read(): Lê o arquivo inteiro.
readline(): Lê uma linha do arquivo.
readlines(): Lê todas as linhas e retorna uma lista.

# Ler o arquivo inteiro
file = open('exemplo.txt', 'r')
conteudo = file.read()
file.close()

# Ler linha por linha
file = open('exemplo.txt', 'r')
for linha in file:
    print(linha, end='')
file.close()

4. Escrita em Arquivos
Para escrever em um arquivo, você pode usar os métodos write() e writelines():

# Escrever no arquivo (sobrescreve o conteúdo existente)
file = open('exemplo.txt', 'w')
file.write('Olá, mundo!\n')
file.close()

# Acrescentar ao arquivo
file = open('exemplo.txt', 'a')
file.write('Nova linha adicionada.\n')
file.close()

try:
    with open("text1.txt", 'a') as arquivo:
        arquivo.write("Hello World")
except FileExistsError:
    print("O ARQUICO JA EXITE")
"""

