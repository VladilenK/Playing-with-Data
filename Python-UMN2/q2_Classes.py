from enum import Enum

class BookStatus(Enum):
    AVAILABLE = "Available"
    BORROWED = "Borrowed"

class Book():
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.status = BookStatus

    def __str__(self):
        return f"{self.title} by {self.author}"
    
    def get_details(self):
        if self.status in BookStatus:
            return(f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Status: {self.status.value}")
        else:
            return(f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}")
    
    def display_info(self):
        print(self.get_details())

    def update_status(self, status):
        self.status = status


class LibraryMember():
    def __init__(self, name, member_id):
        self.name=name
        self.member_id=member_id
        self.borrowed_books = []

    def __str__(self):
        return f"{self.name}"

    def borrow_book(self, book):
        # Adds a book to borrowed books if available and updates the book’s status to Borrowed
        if book.status == BookStatus.AVAILABLE:
            self.borrowed_books.append(book)
            book.update_status(BookStatus.BORROWED)
            return True

    def return_book(self, book):
        # Removes a book from borrowed books and updates the book’s status to Available
        self.borrowed_books.remove(book)
        book.update_status(BookStatus.AVAILABLE)

    def get_borrowed_books(self):
        return self.borrowed_books
    
    def list_borrowed_books(self):
        # display all books borrowed by the member
        for book in self.borrowed_books:
            print(" - ", book.get_details())
    

class Library():
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        book.status = BookStatus.AVAILABLE
        self.books.append(book)

    def remove_book(self, isbn):
        book = next((book for book in self.books if book.isbn == isbn), None)
        if book:
            self.books.remove(book)
            return True
        else:
            return False

    def search_book_by_title(self, title):
        for book in self.books: 
            if title.lower() == book.title.lower():
                return book

    def list_all_books(self):
        # display all books in the library with their status
        for book in self.books:
            print(" - ", book.get_details())
        
    
    def __str__(self):
        return f"Library: {self.name}"

