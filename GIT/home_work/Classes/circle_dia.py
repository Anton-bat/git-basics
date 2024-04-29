class Circle:
    pi = 3.14

    def __init__(self, radius) -> None:
        self.radius = radius

    def area(self):
        return self.pi * (self.radius **2)
    
    @classmethod
    def from_diameter(cls, diameter):
        radius = diameter / 2
        return cls(radius)

    @staticmethod
    def check_radius(radius):
        return radius > 0


circl = Circle.from_diameter(10)
print(circl.area())
print(Circle.check_radius(17))



