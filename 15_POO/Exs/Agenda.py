from datetime import date
from Pessoa import Pessoa


class Agenda:

    def __init__(self):
        self.__contatos: list[Pessoa] = []

    @property
    def contatos(self) -> list[Pessoa]:
        return self.__contatos

    def new_contact(self, contact: Pessoa) -> None:
        self.contatos.append(contact)

    def remove_contact(self, contact: Pessoa) -> None:
        self.contatos.remove(contact)

    def search_contact(self, name: str) -> None:
        for inx, contact in enumerate(self.contatos):
            if contact.name == name:
                print(f"THE CONTACT {name} is the position {inx}")

    def print_agenda(self) -> None:
        for contact in self.contatos:
            contact.print_dados()
            print("---------------------")

    def search_inx(self, inx: int) -> None:
        self.contatos[inx].print_dados()

if __name__ == '__main__':
    contato1: Pessoa = Pessoa("Steve Jobs", date(1996,1,12), "marlonsalles@")
    contato2: Pessoa = Pessoa("Ray Penber", date(1955,1,12), "marlonsalles@")
    contato3: Pessoa = Pessoa("Silicon valey", date(1699,12,12), "marlonsalles@")

    agenda: Agenda = Agenda()
    agenda.new_contact(contato1)
    agenda.new_contact(contato2)
    agenda.new_contact(contato3)

    agenda.print_agenda()
    agenda.search_contact("Steve Jobs")
    agenda.remove_contact(contato1)
    agenda.print_agenda()






