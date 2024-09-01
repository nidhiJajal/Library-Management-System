import unittest
from library_system import Library, Book


class TestLibrarySystem(unittest.TestCase):
    def setUp(self):
        self.library = Library()
        self.book1 = Book(isbn="1234567890", title="The Great Gatsby", author="F. Scott Fitzgerald", publication_year=1925)
        self.book2 = Book(isbn="0987654321", title="1984", author="George Orwell", publication_year=1949)
        self.library.add_book(self.book1)
        self.library.add_book(self.book2)

    def test_add_book_success(self):
        book3 = Book(isbn="1122334455", title="To Kill a Mockingbird", author="Harper Lee", publication_year=1960)
        self.library.add_book(book3)
        self.assertIn("1122334455", self.library.books)

    def test_add_book_duplicate(self):
        with self.assertRaises(ValueError):
            self.library.add_book(self.book1)

    def test_borrow_book_success(self):
        self.library.borrow_book("1234567890")
        self.assertTrue(self.library.books["1234567890"].is_borrowed)

    def test_borrow_book_unavailable(self):
        self.library.borrow_book("1234567890")
        with self.assertRaises(ValueError):
            self.library.borrow_book("1234567890")

    def test_return_book_success(self):
        self.library.borrow_book("1234567890")
        self.library.return_book("1234567890")
        self.assertFalse(self.library.books["1234567890"].is_borrowed)

    def test_return_book_not_borrowed(self):
        with self.assertRaises(ValueError):
            self.library.return_book("1234567890")

    def test_view_available_books(self):
        self.library.borrow_book("1234567890")
        available_books = self.library.view_available_books()
        self.assertEqual(len(available_books), 1)
        self.assertEqual(available_books[0].isbn, "0987654321")


if __name__ == '__main__':
    unittest.main()
