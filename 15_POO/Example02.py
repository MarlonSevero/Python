"""

class Usuario:

    @classmethod        #Metodo de Classe
    def usercount(cls):
        print(f'{cls.contador}')

    @classmethod
    def teste(cls):
        print('teste')

    @staticmethod
    def codee():
        return 'XRXS092'

    contador = 0

    def __init__(self, name, second, mail, passwd):
        self.__id = Usuario.contador + 1
        self.__name = name
        self.__second = second
        self.__mail = mail
        self.__passwd = crypt.hash(passwd)
        Usuario.contador = self.__id
        print(f'User {Usuario.__new_user(self)} created')

    def nome_completo(self):
        return f'{self.__name} {self.__second}'

    def check_passwd(self, passwd):
        if crypt.verify(passwd, self.__passwd):
            return True
        else:
            return exit(41)
    def __new_user(self): #Metodo privado
        return self.__mail.split('@')[0]
"""


class Sapato:

    def __init__(self, tam, cor, descricao):
        pass


