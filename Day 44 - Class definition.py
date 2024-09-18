"""
Day 44 - Class definition
Create a class for a book with attributes like title and author.
"""

class Book:
    def __init__(self, author, title) -> None:
        self.title = title
        self.author = author

    def printBook(self):
        print(f"Author: {self.author}. Title: {self.title}")

book1 = Book("Chris","Python")

book1.printBook()
