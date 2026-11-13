class Book:
    genre = []
    title = ""
    author = ""
    publication_date = ""
    edition = ""
    age_limit = 0
    isbn = ""
    borrowed = False
    reserved = False
    available = True


    def __init__(self, genre, title, author, publication_date, edition, age_limit, isbn, borrowed, reserved, available):
        self.genre = genre
        self.title = title
        self.author = author
        self.publication_date = publication_date
        self.edition = edition
        self.age_limit = age_limit
        self.isbn = isbn
        self.borrowed = borrowed
        self.reserved = reserved
        self.available = available


    def is_available(self):
        if not self.borrowed:
            available = True
        else:
            available = False
        return available


    def reserve_book(self):
        self.reserved = True