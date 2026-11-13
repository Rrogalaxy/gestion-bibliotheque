from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.types import Date, String

from classes.base import Base
from classes.borrowings import Borrowing


class Client(Base):
    __tablename__ = "clients"
    id: Mapped[int] = mapped_column(primary_key=True)
    lastname: Mapped[str] = mapped_column(String(50))
    firstname: Mapped[str] = mapped_column(String(30))
    email: Mapped[str] = mapped_column(String(255))
    phone: Mapped[str] = mapped_column(String(10))
    address: Mapped[str] = mapped_column(String(255))
    birthdate: Mapped[Date] = mapped_column(Date)

    borrowings_history = []
    reserved_books = []

    def __init__(
        self,
        firstname,
        lastname,
        birthdate,
        email,
        phone,
        address,
        borrowings_history,
        reserved_books,
    ):
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
