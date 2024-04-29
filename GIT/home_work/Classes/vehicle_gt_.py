class Vehicle:

    def __init__(self, brand, speed, cost) -> None:
        self.brand = brand
        self.speed = speed
        self.cost = cost

    def __gt__(self, other):
        if isinstance(other, Vehicle):
            return self.speed > other.speed

v1 = Vehicle("Name1", 100, 10000)
v2 = Vehicle("Name2", 110, 9000)

result = sorted([v1, v2])

print(v1 > v2)


