from sqlalchemy.orm import Mapped, mapped_column

from classes.base import Base


class Category(Base):
    # newpaper, novel, documentary, comic book, ...
    __tablename__ = "categories"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True)
