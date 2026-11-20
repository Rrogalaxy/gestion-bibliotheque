from sqlalchemy import Column, ForeignKey, Table

from classes.base import Base

book_genre: Table = Table(
    "book_genre",
    Base.metadata,
    Column("book_id", ForeignKey("books.id"), primary_key=True),
    Column("genre_id", ForeignKey("genres.id"), primary_key=True),
)
