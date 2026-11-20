from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship

from classes.base import Base
from classes.books.book_genre import book_genre

if TYPE_CHECKING:
    # only evaluated by the type checker, never at runtime
    from classes.books.book import Book


class Genre(Base):
    __tablename__ = "genres"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True)

    books: Mapped[list["Book"]] = relationship(
        secondary=book_genre, back_populates="genres"
    )
