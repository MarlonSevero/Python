"""
POO - Atributos

Atributos representam as caractericas dos objetos.

3 Grupos:

   1 -  *Atributos de Instancia* :
        Sao declarados dentro do metodo constructor
            OBS : metodo contrutor : é um metodo especial utilizada para a contrucao do objeto

        Em python por convensao, ficou estabelicido que todo atributo de uma classe é publico. Ou seja, pode ser acessado
        em todo o projeto.

        Quando precisamos de um atributo privado, ou seja, acessado somente dentro da classe declarada,
        usamos o duplo undercore __

    # Atributos publicos e Privados (Visibilidade)

    # Atributos privados so podem ser acessados dentro da propria classe que ele foi declarado
        MSS = ContaCorrente(1234, 202020, 200000)
        print(MSS._ContaCorrente__limite) #Name Mangling (Temos acesso, mas nao devemos acessar)

    # Classe com Atributos de instancia Publicos
    class Lampada:

        def __init__(self, voltagem, cor):
            self.voltagem = voltagem
            self.cor = cor
            self.ligada = True

    # Classe com Atributos de instancia Privados
    class ContaCorrente:

        def __init__(self, numero, limite, saldo):
            self.numero = numero
            self.__limite = limite
            self.__saldo = saldo

2 - *Atributos de Classe*
    Atributos de classe :

        Atributos de classe, sao atributos que sao declarado diretamente na classe, ou seja,
        fora do contrutor. Geralmente ja iniciazamos um valor, e este valor, é compartilhado entre todas as instancias da
        da classe.
        Ou seja, ao inves de cada instancia ter seus proprios valores, como é o caso de atributos de instancias ,
        com os atributos de classe todas as instancias terao os mesmo valor para este atributo.

    class Produto:
        #Atributo de Classe
        imposto = 0.05
        def __init__(self, nome, preco, valor):
            self.nome = nome
            self.preco = preco
            self.valor = (valor + (valor * Produto.imposto))

atributos Dinamico

"""

#REFATORANDO

class Produto:

    #Atributo de Classe
    imposto = 0.05

    def __init__(self, nome, preco, valor):
        self.nome = nome
        self.preco = preco
        self.valor = (valor + (valor * Produto.imposto))