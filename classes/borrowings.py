from sqlalchemy import Column, ForeignKey, Table

from classes.base import Base

borrowings: Table = Table(
    "borrowings",
    Base.metadata,
    Column("book_id", ForeignKey("books.id"), primary_key=True),
    Column("client_id", ForeignKey("clients.id"), primary_key=True),
)
