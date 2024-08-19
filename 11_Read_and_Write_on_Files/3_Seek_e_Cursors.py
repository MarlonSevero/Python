"""

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