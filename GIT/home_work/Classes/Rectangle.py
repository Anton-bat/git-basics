

class Rectangle:

    def __init__(self, width, long) -> None:
        self.width = width
        self.long = long

    def square(self):
        return self.width * self.long

    def perimeter(self):
        return (self.width + self.long) * 2


rect = Rectangle(2, 4) 
print(rect.square())
print(rect.perimeter())


