"""
O bloco try/except

Utilizamos try/except para tratar erros que podem ocorreno nosso codigo. Previnindo
assim que o programa pare de funcionar e o usuario receba mensagens de erro inesperada.

A forma geral mais simples e:

try:
    //execuçao problematica
except:
    //o que deve ser feito em caso de problema

# Exemplo 1 - Tratando um erro generico.

try:
    geek()
except:
    print('Deu algum problema')

# Tente executar a função geek(), caso você encontre erros, imprima a mensagem de erro.

# Exemplo 2 - Tratando um erro generico.

try:
    len(5)
except:
    print('Deu algum problema')

* OBS: Tratar erro de forma generica não é a melhor forma de tratamento de erro. O ideal
é SEMPRE tratar de forma especifica.

# Exemplo 3 - Tratando um erro especifico.

try:
    geek()
except NameError:
    print('Funcao nao existe')

# Exemplo 4 - Tratando um erro especifico.

try:
    len()
except TypeError:
    print('Funcao nao existe')

# Exemplo 5 - Tratando um erro especifico com detalhes do erro.

try:
    len(5)
except TypeError as err:
    print(f'A aplicação gerou o seguinte erro {err}')

# Podemos efetuar varios tratamentos de erro de uma vez.

# Exemplo 6 - Tratando varios erro especificos com detalhes dos erros.

try:
    print('geek'[9])
except TypeError as erra:
    print(f'A aplicação gerou o seguinte erro {erra}')
except NameError as erra:
    print(f'A aplicação gerou o seguinte erro {erra}')
except:
    print('Deu um erro diferente')

# Exemplo 7 - Tratando varios erro especificos dentro das funções.

def pega_valor(dicionario, chave):
    try:
        return  dicionario[chave]
    except KeyError:
        return None
    except NameError:
        return None

dict = {7:'valor'}

print(pega_valor(dict, 'chave'))

"""

def pega_valor(dicionario, chave):
    try:
        return dicionario[chave]
    except KeyError:
        return None
    except NameError:
        return None


dict = {7: 'valor'}

print(pega_valor(dict, 'chave'))











