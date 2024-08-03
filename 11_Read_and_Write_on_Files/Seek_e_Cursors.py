
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

Claro! Vamos resumir a função `seek()` em Python e como ela se relaciona com cursores de arquivos.

### Função `seek()`

A função `seek()` em Python é usada para mover o cursor de leitura/escrita em um arquivo. Ela permite acessar uma posição específica no arquivo para ler ou escrever dados a partir dessa posição.

#### Sintaxe
```python
file.seek(offset, whence)
```

- **`offset`**: O número de bytes a ser movido a partir da posição especificada por `whence`.
- **`whence`**: (Opcional) Define a partir de onde o `offset` deve ser contado:
  - `0` (ou `os.SEEK_SET`): A partir do início do arquivo.
  - `1` (ou `os.SEEK_CUR`): A partir da posição atual do cursor.
  - `2` (ou `os.SEEK_END`): A partir do final do arquivo.

#### Exemplos

1. **Mover para o Início**
   ```python
   with open('example.txt', 'rb') as file:
       file.seek(0)       # Move o cursor para o início do arquivo
       data = file.read() # Lê o conteúdo do arquivo a partir do início
   ```

2. **Mover para uma Posição Específica**
   ```python
   with open('example.txt', 'rb') as file:
       file.seek(10)      # Move o cursor para a posição 10 a partir do início
       data = file.read(5) # Lê 5 bytes a partir da posição 10
   ```

3. **Mover Relativamente ao Final do Arquivo**
   ```python
   with open('example.txt', 'rb') as file:
       file.seek(-5, 2)   # Move o cursor 5 bytes antes do final do arquivo
       data = file.read() # Lê o conteúdo a partir dessa posição até o final
   ```

### Cursores de Arquivo

- **Cursor de Leitura/Escrita**: O cursor é a posição atual dentro do arquivo onde as próximas operações de
leitura ou escrita ocorrerão. A função `seek()` move esse cursor para a posição desejada.

- **Leitura e Escrita**: Após usar `seek()` para posicionar o cursor, você pode usar funções como `read()`,
`write()`, etc., para operar a partir dessa posição.

- **Posição Atual**: Para obter a posição atual do cursor, você pode usar `file.tell()`:
  ```python
  with open('example.txt', 'rb') as file:
      file.seek(10)
      print(file.tell())  # Imprime a posição atual do cursor, que será 10
  ```

### Considerações

- **Modos de Abertura**: `seek()` é mais comumente usado com arquivos binários (`'rb'`, `'wb'`). Para arquivos de
texto, a manipulação de posições pode ser menos direta devido à codificação e a possíveis quebras de linha.

- **Função `tell()`**: Junto com `seek()`, a função `tell()` pode ser usada para rastrear e verificar a posição
atual do cursor no arquivo.

A função `seek()` é essencial para operações que exigem acesso aleatório a dados em arquivos, permitindo
manipulações precisas e eficientes.

"""
#open()
#read


arquivo = open('text.txt')
linhas = arquivo.readlines()
print(len(linhas))