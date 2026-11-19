from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from classes.base import Base


class Edition(Base):
    __tablename__ = "editions"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255))
