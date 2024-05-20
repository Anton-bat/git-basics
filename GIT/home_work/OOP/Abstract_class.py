from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    # @abstractmethod
    # def perimeter(self):
    #     pass

class Rectangle(Shape):
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius) -> None:
        self.radius = radius
    
    def area(self):
        return 3.14 * (self.radius ** 2)
    
circ = Circle(6)
rect = Rectangle(2, 8)

print(circ.area())
print(rect.area())


