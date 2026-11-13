from sqlalchemy import create_engine

from classes import base, books, clients, librarians

if __name__ == "__main__":
    engine = create_engine("sqlite:///library.db")
    base.Base.metadata.create_all(engine)
