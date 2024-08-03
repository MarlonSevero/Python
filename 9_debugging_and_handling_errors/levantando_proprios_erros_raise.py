"""
Levantando os proprios erros com raise

raise -> Lança exceções

OBS: O raise não é uma função. É uma palavra reservada, assim como def ou qualquer
outra em Python.

Para simplificar, pense no raise como sendo util para que possamos criar nossas exceções
e mensagens de erro.

A forma geral de utilização é:

raise TipoDoErro('Mensagem de Erro')

def colore(texto, cor):
    if type(texto) is not str:
        raise TypeError("texto precisa ser uma string")
    if type(cor) is not str:
        raise TypeError("cor precisa ser uma string")
    print(f'O texto {texto} será impresso em {cor}')

colore('True', 7)


# Exemplo Real 02

def colore(texto, cor):
    cores = ('verde', 'azul', 'amarelo')
    if type(texto) is not str:
        raise TypeError("texto precisa ser uma string")
    if type(cor) is not str:
        raise TypeError("cor precisa ser uma string")
    if cor not in cores:
        raise ValueError(f'A cor precisa ser uma entre {cores}')
    print(f'O texto {texto} será impresso em {cor}')
colore('Olaaa', 'verde')

* Lembrando, não estamos tratando o erro e sim lançando.

OBS: O raise, assim como o return, finaliza a funcao.Ou seja, nada apos o raise e
executado.

OBS: Quando falasse em lancar erros, estamos falando de lancar uma execessao
erro e execcao e a mesma coisa.



"""

















