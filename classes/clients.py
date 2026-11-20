from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.types import Date, String

from classes.base import Base

if TYPE_CHECKING:
    from classes.books import book

from classes.borrowings import borrowings


class Client(Base):
    __tablename__ = "clients"
    id: Mapped[int] = mapped_column(primary_key=True)
    lastname: Mapped[str] = mapped_column(String(50))
    firstname: Mapped[str] = mapped_column(String(30))
    email: Mapped[str] = mapped_column(String(255))
    phone: Mapped[str] = mapped_column(String(10))
    address: Mapped[str] = mapped_column(String(255))
    birthdate: Mapped[Date] = mapped_column(Date)

    books: Mapped[list["book.Book"]] = relationship(
        secondary=borrowings, back_populates="clients"
    )
