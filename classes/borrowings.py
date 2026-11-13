from datetime import date


class Borrowing:
    borrowed_book = []
    # borrow_date = date(0, 0, 0)
    # return_date = date(0, 0, 0)

    is_overdue = False

    def __init__(self, book, borrow_date, return_date):
        self.borrowed_book = [book]
        self.borrow_date = borrow_date
        self.return_date = return_date

        if date.today() > self.return_date:
            self.is_overdue = True

    def add_book(self, book):
        self.borrowed_book.append(book)
