from sqlalchemy import Column, ForeignKey, String, Table, create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class Clients(Base):
    __tablename__ = "clients"
    id: Mapped[int] = mapped_column(primary_key=True)
    last_name: Mapped[str] = mapped_column(String(50))
    first_name: Mapped[str] = mapped_column(String(30))
    email: Mapped[str] = mapped_column(String(255))
    phone_number: Mapped[str] = mapped_column(String(10))
    address: Mapped[str] = mapped_column(String(255))


class Librarian(Base):
    __tablename__ = "librarian"
    id: Mapped[int] = mapped_column(primary_key=True)
    last_name: Mapped[str] = mapped_column(String(50))
    first_name: Mapped[str] = mapped_column(String(30))
    email: Mapped[str] = mapped_column(String(255))
    password: Mapped[str]


# association table: one row = one (book, genre) pair
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


class Author(Base):
    __tablename__ = "authors"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255))

    # one author -> many books
    books: Mapped[list["Book"]] = relationship(back_populates="author")


class Edition(Base):
    __tablename__ = "editions"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255))

    # one edition -> many books
    books: Mapped[list["Book"]] = relationship(back_populates="edition")


class Genre(Base):
    __tablename__ = "genres"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True)

    # many-to-many through the association table
    books: Mapped[list["Book"]] = relationship(
        secondary=book_genre, back_populates="genres"
    )


class Category(Base):
    # newpaper, novel, documentary, comic book, ...
    __tablename__ = "categories"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True)

    # many-to-many through the association table
    books: Mapped[list["Book"]] = relationship(
        secondary=book_category, back_populates="categories"
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
    author: Mapped["Author"] = relationship(back_populates="books")
    edition: Mapped["Edition"] = relationship(back_populates="books")

    genres: Mapped[list["Genre"]] = relationship(
        secondary=book_genre, back_populates="books"
    )
    categories: Mapped[list["Category"]] = relationship(
        secondary=book_category, back_populates="books"
    )


if __name__ == "__main__":
    engine = create_engine("sqlite:///library.db")
    Base.metadata.create_all(engine)
