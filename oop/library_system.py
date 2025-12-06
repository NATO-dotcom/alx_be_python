#!/usr/bin/env python3
"""
library_system.py
Defines classes demonstrating inheritance (Book, EBook, PrintBook) and
composition (Library).
"""

class Book:
    """Base class for all books."""
    def __init__(self, title: str, author: str):
        """Initializes common book attributes."""
        self.title = title
        self.author = author

    def __str__(self):
        """Standard string representation for a generic book."""
        return f"Book: {self.title} by {self.author}"

class EBook(Book):
    """Derived class for digital books."""
    def __init__(self, title: str, author: str, file_size: int):
        """
        Initializes EBook attributes, calling the base class constructor first.
        """
        # Call the base class constructor
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        """String representation including EBook-specific attribute."""
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"

class PrintBook(Book):
    """Derived class for physical printed books."""
    def __init__(self, title: str, author: str, page_count: int):
        """
        Initializes PrintBook attributes, calling the base class constructor first.
        """
        # Call the base class constructor
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        """String representation including PrintBook-specific attribute."""
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"

class Library:
    """
    Demonstrates Composition: A class that holds a collection of Book objects.
    """
    def __init__(self):
        """Initializes the library with an empty list of books."""
        # Composition: The Library object 'has-a' list of books.
        self.books = []

    def add_book(self, book: Book):
        """Adds a Book, EBook, or PrintBook instance to the library."""
        if isinstance(book, Book):
            self.books.append(book)
        else:
            print("Error: Item is not a valid Book type.")

    def list_books(self):
        """Prints the details of each book in the library using their __str__ method."""
        for book in self.books:
            print(book)