class Vehicle:
    def __init__(self, make, model) -> None:
        self.make = make
        self.model = model

    def get_info(self):
        return f'{self.make}, {self.model}'
    
class Electric:
    def __init__(self) -> None:
        self.__battery = 0
    
    def charge(self):
        self.__battery = 100
    
class Car(Vehicle):
    def __init__(self, make, model, wheels) -> None:
        super().__init__(make, model)
        self.wheels = wheels

class Moto(Vehicle):
    def __init__(self, make, model, wheels) -> None:
        super().__init__(make, model)
        self.wheels = wheels

class ElectricCar(Vehicle, Electric):
    def __init__(self, make, model, wheels):
        Vehicle.__init__(self, make, model)
        Electric.__init__(self)
        self.wheels = wheels

class ElectricMoto(Vehicle, Electric):
    def __init__(self, make, model, wheels):
        Vehicle.__init__(self, make, model)
        Electric.__init__(self)
        self.wheels = wheels


car = Car("Skoda", "A7", 4)
moto = Moto("SJ", "ee", 2)
e_car = ElectricCar("Tesla", "S", 4)
e_moto = ElectricMoto("TT", "Q1", 2)

print(car.__class__.mro())
print(moto.__class__.mro())
print(e_car.__class__.mro())
print(e_moto.__class__.mro())