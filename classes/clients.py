from datetime import date
from borrowings import Borrowing

class Client:
    firstname = ""
    lastname = ""
    birthdate = date(0, 0, 0)
    email = ""
    phone = ""
    address = ""
    borrowings_history = []
    reserved_books = []


    def __init__(self, firstname, lastname, birthdate, email, phone, address, borrowings_history, reserved_books):
        self.firstname = firstname
        self.lastname = lastname
        self.birthdate = birthdate
        self.email = email
        self.phone = phone
        self.address = address
        self.borrowings_history = borrowings_history
        self.reserved_books = reserved_books

    def borrow_books(self, books, current_date, return_date):
        borrowing = Borrowing(books, current_date, return_date)
        self.borrowings_history.append(borrowing)

    def reserve_books(self, books):
        for book in books:
            if not book.reserved:
                book.reserve_book()
                self.reserved_books.append(book)