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

class Sapato:

    def __init__(self, tam, cor, descricao):
        pass


01. Crie uma classe Pessoa, contendo nome, data de nascimento e email. Crie as propriedades getters e
setters para os atributos e um método para imprimir os dados de uma pessoa.

class Pessoa:

    def __init__(self, name: str, data_nasc: str, email: str):
        self.name = name
        self.date_nasc = data_nasc
        self.email = email

    def dados(self):
        return self.name, self.date_nasc, self.email

    def change_name(self, value: str):
        self.name = value


person1 = Pessoa("Teste", "01/01/0001", "marconsaves@hotmail.com")
print(person1.dados())
person1.change_name("Joao Pereira")
print(person1.dados())

02.

2. Crie uma classe Agenda que pode armazenar contatos e seja possível realizar as seguintes operações:
a) armazenar_contato(crmazover_contato(contaenar_contato(contato: Contato);ontato: Contato); ok
b) remto: Contato);
c) buscar_contato(nome: str); // Informa em que posição da agenda está o contato.
d) imprimir_agenda(); // Imprime os dados de todos os contatos da agenda. ok
e) imprimir_contato(indice: int); // Imprime os dados do contato informado pelo índice.

from datetime import datetime
from Pessoa import Pessoa


class Agenda:

    def __init__(self):
        self.__contatos: list[Pessoa] = []

    @property
    def contacts(self) -> list[Pessoa]:
        return self.__contatos

    def save_contact(self, contact: Pessoa) -> None:
        self.__contatos.append(contact)

    def delete_contact(self, contact: Pessoa) -> None:
        self.__contatos.remove(contact)

    def search_contact(self, src_name: str) -> None:
        for idx, contact in enumerate(self.contacts):
            if contact.name == src_name:
                print(f"The contact is {src_name} in the position {idx}")
            else:
                print("Not Find!")

    def print_contact(self) -> None:
        for contact in self.contacts:
            print(f"{contact.name}")



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

class Sapato:

    def __init__(self, tam, cor, descricao):
        pass


"""


