from sqlalchemy import Column, ForeignKey, String, Table
from sqlalchemy.orm import Mapped, mapped_column, relationship

from classes.base import Base
from classes.books import author, category, edition, genre

book_genre: Table = Table(
    "book_genre",
    Base.metadata,
    Column("book_id", ForeignKey("books.id"), primary_key=True),
    Column("genre_id", ForeignKey("genres.id"), primary_key=True),
)

# association table: one row = one (book, category) pair
book_category: Table = Table(
    "book_category",
    Base.metadata,
    Column("book_id", ForeignKey("books.id"), primary_key=True),
    Column("category_id", ForeignKey("categories.id"), primary_key=True),
)


class Book(Base):
    __tablename__ = "books"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(255))
    isbn: Mapped[str] = mapped_column(unique=True)
    description: Mapped[str]
    age_limit: Mapped[int]

    # foreign key: the actual column stored in the table
    author_id: Mapped[int] = mapped_column(ForeignKey("authors.id"))
    edition_id: Mapped[int] = mapped_column(ForeignKey("editions.id"))

    # Python-side navigation, no column created
    author: Mapped["author.Author"] = relationship(back_populates="books")
    edition: Mapped["edition.Edition"] = relationship(back_populates="books")

    genres: Mapped[list["genre.Genre"]] = relationship(
        secondary=book_genre, back_populates="books"
    )
    categories: Mapped[list["category.Category"]] = relationship(
        secondary=book_category, back_populates="books"
    )
    borrowed = False
    reserved = False
    available = True

    def __init__(
        self,
        genre,
        title,
        author,
        publication_date,
        edition,
        age_limit,
        isbn,
        borrowed,
        reserved,
        available,
    ):
        self.genre = genre
        self.title = title
        self.author = author
        self.publication_date = publication_date
        self.edition = edition
        self.age_limit = age_limit
        self.isbn = isbn
        self.borrowed = borrowed
        self.reserved = reserved
        self.available = available

    def is_available(self):
        if not self.borrowed:
            available = True
        else:
            available = False
        return available

    def reserve_book(self):
        self.reserved = True
