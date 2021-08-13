class Book:

    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __repr__(self):
        return f"'{self.title}' by {self.author}"

    def __lt__(self, other):
        return self.title < other.title


class Borrower:

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name


class Library:

    def __init__(self):
        # All books owned by the library
        self.books_collection: list[Book] = []
        # Only books available to be borrowed
        self.books_available: list[Book] = []
        self.borrowed_books = {}

    def add_book(self, book: Book) -> None:
        """"Add book to Library"""
        self.books_collection.append(book)
        self.books_collection.sort()
        self.books_available.append(book)
        self.books_available.sort()

    def add_books(self, books: list[Book]) -> None:
        """Add list of books to Library"""
        for book in books:
            self.add_book(book)

    def lend_book_to(self, borrower: Borrower, book: Book) -> None:
        """ Lend book to people"""
        if book not in self.books_available:
            raise Exception("Book is not available")

        borrowers = self.borrowed_books.keys()

        if borrower in borrowers:
            self.borrowed_books[borrower].append(book)
        else:
            self.borrowed_books[borrower] = [book]

        self.books_available.remove(book)

    def lend_books_to(self, borrower: Borrower, books: list[Book]):
        """ Lend books to people"""
        for book in books:
            self.lend_book_to(borrower, book)

    def receive_borrowed_book(self, borrower: Borrower, book: Book) -> None:
        borrower_borrowed_books = self.borrowed_books[borrower]

        if book in borrower_borrowed_books:
            self.books_available.append(book)
            self.books_available.sort()
            borrower_borrowed_books.remove(book)

        else:
            raise Exception(f"{book} was not lent to borrower")

        if not self.borrowed_books[borrower]:
            self.borrowed_books.pop(borrower)

    def receive_borrowed_books(self, borrower: Borrower, books: list[Book]) -> None:
        for book in books:
            self.receive_borrowed_book(borrower, book)

    def books_lent(self):
        if self.borrowed_books:
            print(self.borrowed_books)
        else:
            print("None")


if __name__ == "__main__":
    pass
    # library = Library()
    #
    # harry_potter = Book('Harry Potter', 'J. K. Rowling')
    # LOTR = Book('Lord of the Rings', ' J. R. R. Tolkien')
    # GOT = Book('Game of Thrones', 'George R. R. Martin')
    # americannah = Book("Americannah", 'Chimamanda Ngozi')
    #
    # # print(library.books_collection)
    #
    # library.add_books([harry_potter, LOTR, GOT, americannah])
    # # print(library.books_available)
    #
    # quame = Borrower('Quame Jnr')
    #
    # library.lend_book_to(quame, LOTR)
    # library.lend_books_to(quame, [GOT, harry_potter])
    #
    # print(library.books_available)
    # library.receive_borrowed_book(quame, LOTR)
    # library.receive_borrowed_books(quame, [GOT, americannah])
    # print(library.books_available)
