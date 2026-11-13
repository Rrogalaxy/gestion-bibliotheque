from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from classes.base import Base


class Librarian(Base):
    __tablename__ = "librarian"
    id: Mapped[int] = mapped_column(primary_key=True)
    lastname: Mapped[str] = mapped_column(String(50))
    firstname: Mapped[str] = mapped_column(String(30))
    email: Mapped[str] = mapped_column(String(255))
    password: Mapped[str]

    def __init__(self, firstname, lastname, email):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
