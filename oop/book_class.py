#!/usr/bin/env python3
"""Defines the Book class with essential magic methods."""

class Book:
    """Models a book with title, author, and year, using magic methods."""
    
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        print(f"Deleting {self.title}")

    def __str__(self):
        """Informal string representation for end-users."""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """Official string representation for debugging/recreation."""
        return f"Book('{self.title}', '{self.author}', {self.year})"