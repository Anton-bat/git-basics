class Book:

    def __init__(self, title, author) -> None:
        self.title = title
        self.author = author

    def __eq__(self, value: object) -> bool:
        return self.title == value.title and self.author == value.author

    def __ne__(self, value: object) -> bool:
        return not self.__eq__(value)

class Library:
    def __init__(self, books) -> None:
        self.books = books

    def __len__(self):
        return len(self.books)
    
    def __getitem__(self, index):
        return self.books[index]

    
b1 = Book("Title1", "Author1")
b2 = Book("Title2", "Author2")
b3 = Book("Title3", "Author3")

library = Library([b1, b2, b3])

print(len(library))
print(library[2])