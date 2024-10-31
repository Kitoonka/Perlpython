# library management system
class Book:
     def __init__(self, title, author):
         self.title = title
         self.author = author
    def displaying_info(self):
            return f"Title: {self.title}, Author: {self.author}"
# child class/derived class
class libraryBook(Book):
    def __init__(self, title, author, year):
        super().__init__(title, author)
        self.isbn = isbn
        self.copies_available=copies_available
        def borrow_book(self):
            if self.copies_available > 0:
                self.copies_available -= 1
                return f"Title: {self.title} borrowed.copiesAvailable={self.copies_available}"
            else:
                return f"No of Title: {self.title} available"
def return_book(self):
        self.copies_avialable +=1
        return f"{self.title} Returned. Copies left {self.copies_avialable}"
# usage example
book1=LibraryBook("Blossoms","Maina Kinani",4565487556,18)
print(book1.displayinfo())

# print(book1.borrow_book())

print(book1.borrow_book())

print(book1.return_book())

