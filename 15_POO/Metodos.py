"""
POO - Metodos

- Metodos (funcoes) - Representamn o  comportamento do objeto. Ou seja, as acoes que este objeto pode realizar no seu
sistema.

Em Python dividimos os Metodos , assim como os atributos, Metodos de instandcia e Metodos de Classe.

Metodos de instancia:

__init__ : O metodo dunder init e um metodo esopecialv chamado de construtor, e tem como objetivo,\
 contruir o objeto atraves da classe.

 OBS: Todo elemento em Python que inicia e finaliza com duplo underline é chamado de dunder (Double Underline)

 OBS: Os metodos Dunder em Python, sao chamados de metodos magicos.


"""


class Lampada:
    def __init__(self, luz, voltagem, luminosidade):
        self.__luz = luz
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.ligada = False


class ContaCorrete:
    contador = 4999
    def __init__(self, limite, saldo):
        self.__numero = ContaCorrete.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        ContaCorrete.contador = self.__numero


class Produto:
    contador = 0

    def __init__(self, nome, valor, desc):
        self.__id = Produto.contador + 1
        self.__nome = nome
        self.__desc = desc
        self.__valor = valor
        Produto.contador = self.__id

    def desconto(self, porcentagem):
        return self.__valor * (100 - porcentagem) / 100


ps3 = Produto("teste", 3000, 10)
print(ps3.desconto(10))