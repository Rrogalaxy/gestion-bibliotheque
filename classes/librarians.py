from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from classes.base import Base


class Librarian(Base):
    __tablename__ = "librarians"
    id: Mapped[int] = mapped_column(primary_key=True)
    lastname: Mapped[str] = mapped_column(String(50))
    firstname: Mapped[str] = mapped_column(String(30))
    email: Mapped[str] = mapped_column(String(255))
    password: Mapped[str] = mapped_column(String(255))


def add():
    pass
