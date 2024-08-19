"""



"""


class BankAccount:
    contador = 0

    def __init__(self, titular, saldo, limite):
        self.id = BankAccount.contador
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        BankAccount.contador += 1

    def extrato(self):
        print(f'O titular {self.__titular} tem o montante de {self.__saldo} e limite de {self.__limite}')

    def deposito(self, valor):
        if valor > 0:
            self.__saldo += valor
        else:
            print('O valor precisa ser maior que zero!')

    def saque(self, valor):
        if valor > 0:
            if valor >= self.__saldo:
                self.__saldo -= valor
            else:
                print('Limite Insuficiente!')
        else:
            print('O valor precisa ser Positivo')


client1 = BankAccount('Marlon Severo', 2000000000000, 9999999999999)
print(client1.extrato())
