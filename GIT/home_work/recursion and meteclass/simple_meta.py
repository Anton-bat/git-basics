class MyMeta(type):
    def __new__(cls, name, bases, attrs):
        print("Making class obj")
        return super().__new__(cls, name, bases, attrs)
    
    def __init__(self, name, bases, attrs):
        print("Init class")
        super().__init__(name, bases, attrs)

class MyClass(metaclass=MyMeta):
    pass
