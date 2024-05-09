# book.py
from models import Book

class BookManagement:
    def __init__(self):
        self.books = []

    def add_book(self, title, author, isbn):
        self.books.append(Book(title, author, isbn))

    def list_books(self):
        for book in self.books:
            print(f"Title: {book.title}, Author: {book.author}, ISBN: {book.isbn}")
