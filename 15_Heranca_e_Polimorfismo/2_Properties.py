"""
POO - Propriedades (Properties)

Getters e Setters

#Getters obtem os valores
#Setters podem setar novos valores (nem sempre aplica)
#Porem isso é mais utilizado em Java, no Python é mais ideal usar as Propriedades.

class Conta:
    contador = 9383
    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador + 1
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    def extrato(self):
        return f'Conta: {self.__numero} Saldo: {self.__saldo} do cliente {self.__titular} e limite de {self.__limite}'

    def depositar(self, value):
         self.__saldo += value

    def sacar(self, value):
        self.__saldo -= value

    def transferir(self, value, destino):
        self.__saldo -= value
        destino.__saldo += value

#Getters
    def get_numero(self):
        return self.__numero
    def get_titular(self):
        return self.__titular
    def get_saldo(self):
        return self.__saldo
    def get_limite(self):
        return self.__limite

#Setters

    def set_limite(self):
        value = int(input('Qual valor de limite? >> '))
        self.__limite += value
        return f'{self.__titular} Novo Limite da sua conta é {self.__limite} '


-----------REFATORANDO



"""


class Conta:
    contador = 9383

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador + 1
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    @property
    def numero(self):
        return self.__numero

    @property
    def titular(self):
        return self.__titular

    @property
    def saldo(self):
        return self.__saldo

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, new_limit):
        self.__limite = new_limit

    @property  #Ps nao é funcao, e sim uma propriedade
    def total(self):
        return f'O valor total da conta {self.__numero} da {self.__titular} é de {self.__saldo + self.__limite}'


    def extrato(self):
        return f'Conta: {self.__numero} Saldo: {self.__saldo} do cliente {self.__titular} e limite de {self.__limite}'

    def depositar(self, value):
         self.__saldo += value

    def sacar(self, value):
        self.__saldo -= value

    def transferir(self, value, destino):
        self.__saldo -= value
        destino.__saldo += value


conta1 = Conta('Angelina', 3000, 5000)
conta2 = Conta('Marcia', 1000, 2000)

print(conta1.extrato())
print(conta2.extrato())

print(conta2.saldo + conta1.saldo) #Elimina a necessidade dos parenteses

conta2.limite = 5000
print(conta2.extrato())


#Nos sempre criamos os atributos privados, se precisarmos acessar / alterar dados dai pensamos em criar os getters e setters.

#Podemos criar metodos como propriedades.

print(conta2.total)
