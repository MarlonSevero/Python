
"""
A função open() em Python é usada para abrir arquivos e retorna um objeto de arquivo, que pode ser usado para ler, escrever e manipular o arquivo. É uma função fundamental para a entrada e saída de dados em programas Python. Aqui está um resumo de como ela funciona, junto com exemplos para ilustrar seu uso:

Resumo da Função open()
A função open() tem a seguinte assinatura:

open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)

file: O caminho do arquivo que você deseja abrir.

mode: O modo em que o arquivo será aberto. Os modos comuns são {
    'r': Leitura (padrão). O arquivo deve existir.
    'w': Escrita. Cria um novo arquivo ou substitui o existente.
    'a': Adição. Adiciona ao final do arquivo se ele existir.
    'b': Modo binário. Pode ser combinado com outros modos (e.g., 'rb' para leitura binária).
    't': Modo texto (padrão). Pode ser combinado com outros modos (e.g., 'rt' para leitura de texto).
    }

buffering: Controla o buffering. O valor -1 usa o buffering padrão, 0 não usa buffering, e qualquer valor
positivo especifica o tamanho do buffer.
encoding: Define a codificação do arquivo (por exemplo, 'utf-8').
errors: Define como lidar com erros de codificação.
newline: Controla como as quebras de linha são interpretadas.
closefd: Se o descritor de arquivo deve ser fechado quando o arquivo é fechado.
opener: Função personalizada para abrir o arquivo.


"""

