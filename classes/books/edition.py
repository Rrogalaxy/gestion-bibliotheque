from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from classes.base import Base

if TYPE_CHECKING:
    # only evaluated by the type checker, never at runtime
    from classes.books.book import Book


class Edition(Base):
    __tablename__ = "editions"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255))

    books: Mapped[list["Book"]] = relationship(back_populates="editions")
