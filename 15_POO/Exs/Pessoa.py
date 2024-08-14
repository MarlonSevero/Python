from datetime import date


class Pessoa:
    count: int = 0

    def __init__(self, name: str, born: date, email: str) -> None:
        self.__name: str = name
        self.__born: date = born
        self.__email: str = email

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        self.__name = name

    @property
    def born(self) -> date:
        return self.__born

    @born.setter
    def born(self, born: int):
        self.__born = born

    @property
    def email(self) -> str:
        return self.__email

    @email.setter
    def email(self, email: str):
        self.__email = email

    def print_dados(self) -> None:
        print(f"Name: {self.name}")
        print(f"Data Nascimento: {self.__born.strftime('%d/%m/%Y')}")
        print(f"Email: {self.__email}")


if __name__ == '__main__':
    ps1 = Pessoa("Teste", date(1989, 1, 31), "marlonsaves@")
