from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from classes.base import Base
from classes.books import author, category, edition, genre
from classes.books.book_genre import book_genre
from classes.borrowings import borrowings

if TYPE_CHECKING:
    from classes.clients import Client

# association table: one row = one (book, category) pair


class Book(Base):
    __tablename__ = "books"

    id: Mapped[int] = mapped_column(
        primary_key=True,
    )
    title: Mapped[str] = mapped_column(String(255))
    isbn: Mapped[str] = mapped_column(unique=True)
    description: Mapped[str]
    age_limit: Mapped[int]

    # foreign key: the actual column stored in the table
    author_id: Mapped[int] = mapped_column(ForeignKey("authors.id"))
    edition_id: Mapped[int] = mapped_column(ForeignKey("editions.id"))
    category_id: Mapped[int] = mapped_column(ForeignKey("categories.id"))

    # Python-side navigation, no column created
    author: Mapped["author.Author"] = relationship(back_populates="books")
    edition: Mapped["edition.Edition"] = relationship(back_populates="books")
    category: Mapped["category.Category"] = relationship(back_populates="books")

    genres: Mapped[list["genre.Genre"]] = relationship(
        secondary=book_genre, back_populates="books"
    )
    clients: Mapped[list["Client"]] = relationship(
        secondary=borrowings, back_populates="books"
    )
