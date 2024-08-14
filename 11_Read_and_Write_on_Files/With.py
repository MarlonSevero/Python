
"""

Claro! A função `with` em Python é usada para simplificar o gerenciamento de recursos, como arquivos.
Quando você usa a declaração `with`, o Python garante que os recursos sejam corretamente liberados
após o uso, mesmo que ocorra uma exceção durante a execução do código. Isso é especialmente útil
para operações com arquivos.

Aqui está um exemplo básico de como usar `with` para abrir e ler um arquivo:

```python
with open('meuarquivo.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    print(conteudo)
```

### Como funciona?

1. **Abertura do Arquivo**: `open('meuarquivo.txt', 'r')` abre o arquivo no modo de leitura (`'r'`).
2. **Gerenciamento do Arquivo**: O objeto retornado pela função `open` é atribuído à variável `arquivo`.
3. **Uso do Arquivo**: O código dentro do bloco `with` pode usar o arquivo, como ler seu conteúdo ou escrever nele.
4. **Fechamento do Arquivo**: Quando o bloco `with` é concluído, o método `__exit__` do objeto de arquivo é
chamado automaticamente, fechando o arquivo, independentemente de como o bloco foi concluído
(com sucesso ou por causa de uma exceção).

### Por que usar `with`?

- **Segurança**: Garante que o arquivo seja fechado corretamente, o que evita vazamentos de recursos e
possíveis problemas com arquivos não fechados.
- **Clareza**: O código é mais limpo e fácil de entender, pois não é necessário chamar manualmente `file.close()`.
- **Exceções**: Se uma exceção ocorrer dentro do bloco `with`, o arquivo ainda será fechado corretamente.

### Exemplo com escrita:

Aqui está um exemplo de como usar `with` para escrever em um arquivo:

```python
with open('meuarquivo.txt', 'w') as arquivo:
    arquivo.write('Olá, mundo!')
```

Neste caso, o arquivo é aberto no modo de escrita (`'w'`). O conteúdo `Olá, mundo!` é escrito no arquivo, e
o arquivo é fechado automaticamente ao final do bloco `with`.

### Aplicação com outros recursos

A função `with` não é limitada a arquivos. Ela pode ser usada com qualquer objeto que suporte o protocolo de
contexto (`__enter__` e `__exit__`). Isso inclui conexões de banco de dados, threads e outros recursos que
 precisam ser gerenciados.

Por exemplo, ao usar `with` com conexões de banco de dados:

```python
with banco_conexao() as conexao:
    resultado = conexao.executar_query('SELECT * FROM tabela')
    print(resultado)
```

Aqui, `banco_conexao()` é uma função fictícia que retorna um objeto de conexão de banco de dados. O método
`__enter__` abre a conexão e o método `__exit__` a fecha automaticamente.

Essa abordagem torna o código mais robusto e fácil de manter, o que é uma das principais vantagens do uso da
declaração `with` em Python.\

with open('text.txt', 'w') as arq:
    while True:
        frutas = input('Informe a fruta, ou digite sair')
        if frutas != 'Sair':
            arq.write(frutas)
            arq.write('\n')
        else:
            break


"""


with open('text.txt', 'w') as arquivo:
    itens = []
    n = int(input("How many times do you want to write?"))
    for x in range(0, n):
        item_num = input("Informe o primeiro item da compra:")
        itens.append(item_num)
        arquivo.write(item_num)
print(itens)


