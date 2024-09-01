from dataclasses import dataclass
from typing import Dict, List


@dataclass
class Book:
    isbn: str
    title: str
    author: str
    publication_year: int
    is_borrowed: bool = False

    def __str__(self):
        status = 'Borrowed' if self.is_borrowed else 'Available'
        return f"{self.title} by {self.author} ({self.publication_year}) - {status}"


class Library:
    def __init__(self):
        self.books: Dict[str, Book] = {}

    def add_book(self, book: Book) -> None:
        if book.isbn in self.books:
            raise ValueError(f"Book with ISBN {book.isbn} already exists.")
        self.books[book.isbn] = book

    def borrow_book(self, isbn: str) -> None:
        if isbn not in self.books:
            raise ValueError(f"Book with ISBN {isbn} does not exist.")
        if self.books[isbn].is_borrowed:
            raise ValueError(f"Book with ISBN {isbn} is already borrowed.")
        self.books[isbn].is_borrowed = True

    def return_book(self, isbn: str) -> None:
        if isbn not in self.books:
            raise ValueError(f"Book with ISBN {isbn} does not exist.")
        if not self.books[isbn].is_borrowed:
            raise ValueError(f"Book with ISBN {isbn} was not borrowed.")
        self.books[isbn].is_borrowed = False

    def view_available_books(self) -> List[Book]:
        return [book for book in self.books.values() if not book.is_borrowed]
