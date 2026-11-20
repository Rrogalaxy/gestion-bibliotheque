from sqlalchemy import create_engine, insert

from classes import base, borrowings, clients, librarians
from classes.books import author, book, category, edition, genre

if __name__ == "__main__":
    engine = create_engine("sqlite:///library.db")
    base.Base.metadata.create_all(engine)
    with engine.connect() as conn:
        stmt = insert(genre.Genre).values(name="Science-fiction")
        stmt = insert(genre.Genre).values(name="Policier")
        stmt = insert(genre.Genre).values(name="Horreur")
