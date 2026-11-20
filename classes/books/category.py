from typing import TYPE_CHECKING

if TYPE_CHECKING:
    # only evaluated by the type checker, never at runtime
    from classes.books.book import Book

from sqlalchemy.orm import Mapped, mapped_column, relationship

from classes.base import Base


class Category(Base):
    # newpaper, novel, documentary, comic book, ...
    __tablename__ = "categories"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True)
    books: Mapped[list["Book"]] = relationship(back_populates="categories")
