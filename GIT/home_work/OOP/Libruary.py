
class Book:
    _total_copies = 0

    def __init__(self, title, author, isbn, copies) -> None:
        self.title = title
        self.author = author
        self.isbn = isbn
        self.copies = copies
        Book._total_copies += copies

    @classmethod
    def update_total_copies(cls, change):
        cls._total_copies += change

    def check_availability(self):
        return self.copies > 0
    
    def update_copies(self, change):
        self.copies += change
        Book.update_total_copies(change)

    @staticmethod
    def validate_isbn(isbn):
        pass

class User:
    def __init__(self, name, user_id) -> None:
        self.name = name
        self._user_id = user_id
    
    @property
    def user_id(self):
        return self._user_id
    

class Customer(User):
    def __init__(self, name, user_id) -> None:
        super().__init__(name, user_id)
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.check_availability():
            self.borrowed_books.append(book)
            book.update_copies(-1)
        else:
            print("no such book")

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.update_copies(1)

class Employee(User):
    def __init__(self, name, user_id, salary, library) -> None:
        super().__init__(name, user_id)
        self.salary = salary
        self._library = library

        @property
        def library(self):
            return self._library
        
        @staticmethod
        def add_book(book, library):
            library.books.append(book)

        @staticmethod
        def removy_book(book, library):
            library.books.remove(book)
        
        @staticmethod
        def register_user(user, library):
            library.users.append(user)
        
        def find_book_by_isbn(self, isbn):
            for book in self.library.books:
                if book.isbn == isbn:
                    return book
        
        def show_available_books(self):
            for book in self.library.books:
                if book.check_availability():
                    print(book.title)

class Library:
    def __init__(self) -> None:
        self.books = []
        self.users = []

    def register_user(self, user):
        self.users.append(user)
    
    def find_book_by_isbn(self, isbn):
        for book in self.library.books:
            if book.isbn == isbn:
                return book
            
    def show_available_books(self):
            for book in self.library.books:
                if book.check_availability():
                    print(book.title)

book1 = Book("Title1", "Author1", "ISBN12345", 5)
print(book1.check_availability())
book1.update_total_copies(10)
print(book1._total_copies)
print(book1.validate_isbn("ISBN12345")) 
user1 = User("John Doe", "12345")
print(user1.get_info())