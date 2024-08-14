"""
Erros mais comuns em Python

ATENÇÃO! É importante prestar atenção e aprender a ler as saidas de erro gerados pela execução.

traceback = Saida de erros

Os erros mais comuns:

SyntaxError -> Ocorre quando o Python encontra um erro de sintaxe, Ou seja, você escreveu algo que o Python não
reconhece como parte da linguagem.

Exemplos de SyntaxError

a)
def funcao:
    print("Teste")

b)
def = 1

c)
return

2 - NameError -> Ocorre quando uma variável ou função não foi definida.

Exemplos NameError

a)
    print(geek)

b)
    geek()

3 - TypeError -> Ocorre quand uma função/operacao/ação é aplicada a um tipo errado.

Exemplos TypeError

a)

print(len(5))

b)
print('geek' + [1])

c)

4 - IndexError -> Ocorre quando tentamos acessar um elemento em uma lista ou outro tipo de dado indexado
utilizando um indice invalido.

Exemplos TypeError:

a)
lista = ['Geek']
print(lista[2])

b)
lista = ['Geek']
print(lista[2][10])

c)
tupla = ('Geek',)
print(tupla[2][10])

5 - ValueError -> ocorre quando uma função/operação built-in (integrada) recebe um argumento com tipo correto
mas valor inapropriado.

Exemplos ValueError

a)
print(int('Geek'))

6 - KeyError -> Ocorre quando tentamos acessar um dicionário com uma chave que não existe.

Exemplos KeyError

a)
dic = {'python':'university'}
print(dic['geek'])

7 - AttributeError -> Ocorre quando uma variável não tem um atributo/função.

Exemplos AttributeError

a)
tupla(11,20,31,4)
print(tupla.sort())

8 - IndentationError  -> Ocorre quando não respeitamos a indentação no Python(4 Espaços)

OBS: Exceptions e Erros são sinonimos na programação.

OBS: SEMPRE PRESTE ATENÇÃO NO RETORNO DE ERRO.

"TODOS POSSIVEIS ERROS NO PYTHON : https://docs.python.org/3/library/exceptions.html"



























"""