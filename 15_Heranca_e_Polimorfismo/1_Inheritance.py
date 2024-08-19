"""
POO - Heranca (Inheritance)

 A ideia de heranca, é a de  reaproveitar codigo.

 Tambem extender nossas classes.

 Com a heranca apartir de uma classe existente, nos extendemos outra classe que passa a herdar atributos e meteodos
    da classe herdada.

Sempre devemos nos perguntar: existe uma entidade generica o suficiente para enpsular os atributos e metodos comuns
a outras entidades.?

# Por exemplo, em banco temos pessoa fisica e juridica ambas sao `pessoas`

[Classe Pessoa]
Quando uma classe herda de outra classe, a classe herdade é conhecida como Super Classe / Classe Pai

[Classse Worker, Client]
Quando uma classe herda de outras classe, ela é conhecida como SubClasse, classe Filha.




"""



class People:
    def __init__(self, name, secondname, cpf):
        self.__name = name
        self.__sobrenome = secondname
        self.__cpf = cpf

    def full_name(self):
        return f'{self.__name} {self.__sobrenome}'


class Worker(People):               #Cliente herda de pessoa, quando uma classe herda de outra classe. Ela herda todos atributos e metodos.
    def __init__(self, name, secondname, cpf, matricula):
        super().__init__(name, secondname, cpf)         #Acessando o contrutor da super Classe. Podendo usar nome da classe mas nao recomendado
        self.__matricula = matricula

    def full_name(self):
        return f'name: {self._People__name} matricula: {self.__matricula}'      #Override


class Client(People):
    def __init__(self, name, secondname, cpf, conta):
        super().__init__(name, secondname, cpf)
        self.__conta = conta


newClient = Client('Angelina', 'Joly', 9999999, 11111)
newWorker = Worker('Felicity', 'Joly', 111111, 9999999)

print(newClient.__dict__)
print(newWorker.__dict__)

#Sobreescrita de metodos (Overriding)
#Sobreescrita de metodo, ocorre quando reescrevemos/reimplementamos um metodo presente em uma super classe em uma classe filha.

print(newWorker.full_name())
print(newClient.full_name())