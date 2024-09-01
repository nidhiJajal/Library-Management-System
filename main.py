from library_system import Library, Book

# Initialize Library
library = Library()

# Add Books
book1 = Book(isbn="1234567890", title="The Great Gatsby", author="F. Scott Fitzgerald", publication_year=1925)
library.add_book(book1)

# View Available Books
available_books = library.view_available_books()
for book in available_books:
    print(book)

# Borrow a Book
library.borrow_book("1234567890")

# Return a Book
library.return_book("1234567890")
