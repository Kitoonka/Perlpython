# Library management system

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display_info(self):
        return f"Title: {self.title}, Author: {self.author}"


# Child class/derived class
class LibraryBook(Book):
    def __init__(self, title, author, isbn, copies_available):
        super().__init__(title, author)
        self.isbn = isbn
        self.copies_available = copies_available

    def borrow_book(self):
        if self.copies_available > 0:
            self.copies_available -= 1
            return f"Title: {self.title} borrowed. Copies Available = {self.copies_available}"
        else:
            return f"No copies of Title: {self.title} available"

    def return_book(self):
        self.copies_available += 1
        return f"{self.title} returned. Copies left = {self.copies_available}"


# Usage example
book1 = LibraryBook("Blossoms", "Maina Kinani", 4565487556, 18)
print(book1.display_info())
print(book1.borrow_book())
print(book1.return_book())
