class Circle:
    pi = 3.14

    def __init__(self, radius) -> None:
        self.radius = radius


    def area(self):
        return Circle.pi * (self.radius **2)

circl = Circle(10)
print(circl.area())



