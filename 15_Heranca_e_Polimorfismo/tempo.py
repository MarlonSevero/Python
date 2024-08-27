from datetime import date
from typing import List

class Book:
    def __init__(self, title: str, author: str, publication_year: int):
        self.title: str = title
        self.author: str = author
        self.publication_year: int = publication_year
        self.available: bool = True

    def __str__(self):
        status = "Disponível" if self.available else "Indisponível"
        return f"{self.title} por {self.author} ({self.publication_year}) - {status}"


class User:
    _id_counter = 1

    def __init__(self, name: str):
        self.id = User._id_counter
        self.name = name
        self.borrowed_books: List[Book] = []
        User._id_counter += 1

    def borrow_book(self, book: Book):
        try:
            if book.available:
                self.borrowed_books.append(book)
                book.available = False
                print(f"O livro {book.title} foi alugado para {self.name}.")
            else:
                raise ValueError(f"Desculpe, {book.title} não está disponível.")
        except ValueError as e:
            print(e)

    def __str__(self):
        return f"Usuário: {self.name}, ID: {self.id}"


class Library:
    def __init__(self, name: str):
        self.name = name
        self.books: List[Book] = []
        self.users: List[User] = []

    def add_book(self, book: Book):
        try:
            if isinstance(book, Book):
                self.books.append(book)
                print(f"O livro {book.title} foi adicionado ao acervo da biblioteca {self.name}.")
            else:
                raise TypeError("O objeto fornecido não é um livro válido.")
        except TypeError as e:
            print(e)

    def add_user(self, user: User):
        try:
            if isinstance(user, User):
                self.users.append(user)
                print(f"Usuário {user.name} adicionado com sucesso!")
            else:
                raise TypeError("O objeto fornecido não é um usuário válido.")
        except TypeError as e:
            print(e)

    def list_books(self):
        print(f"Livros disponíveis na {self.name}:")
        for book in self.books:
            print(book)

    def list_users(self):
        print(f"Usuários cadastrados na {self.name}:")
        for user in self.users:
            print(user)


def main():
    try:
        library = Library('Biblioteca SJY')

        book1 = Book('Romeu e Julieta', 'William Shakespeare', 1597)
        book2 = Book('O Senhor dos Anéis', 'J.R.R. Tolkien', 1954)
        book3 = Book('A Procura da Felicidade', 'Chris Gardner', 2006)

        library.add_book(book1)
        library.add_book(book2)
        library.add_book(book3)

        print('Bem-vindo à Biblioteca SJY!')

        while True:
            try:
                option = int(input('O que você deseja fazer?\n1- Doar um livro\n2- Se cadastrar\n3- Emprestar um livro\n4- Mostrar todos os livros\n5- Mostrar todos os usuários\n6- Sair\nEscolha uma opção: '))

                if option == 1:
                    title = input('Informe o título: ')
                    author = input('Informe o autor: ')
                    publication_year = int(input('Informe o ano de publicação: '))
                    new_book = Book(title, author, publication_year)
                    library.add_book(new_book)

                elif option == 2:
                    name = input('Informe seu nome: ')
                    new_user = User(name)
                    library.add_user(new_user)

                elif option == 3:
                    search_title = input('Informe o título do livro que deseja alugar: ')
                    for book in library.books:
                        if book.title.lower() == search_title.lower():
                            current_user = input('Informe seu nome: ')
                            user = next((u for u in library.users if u.name == current_user), None)
                            if user:
                                user.borrow_book(book)
                            else:
                                raise LookupError("Usuário não encontrado. Cadastre-se primeiro.")
                            break
                    else:
                        raise LookupError("Livro não encontrado.")

                elif option == 4:
                    library.list_books()

                elif option == 5:
                    library.list_users()

                elif option == 6:
                    print('Saindo...')
                    break

                else:
                    raise ValueError('Opção inválida, tente novamente.')

            except ValueError as e:
                print(e)
            except LookupError as e:
                print(e)

    except Exception as e:
        print(f"Erro inesperado: {e}")


if __name__ == "__main__":
    main()