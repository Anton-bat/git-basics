class RenameAttributesMeta(type):
    def __new__(cls, name, bases, attrs):
        new_attrs = {}
        for attr_name, attr_value in attrs.items():
            if attr_name.startswith('__'):
                new_attrs[f'__private_{attr_name[2:]}'] = attr_value
            else:
                new_attrs[attr_name] = attr_value
        return super().__new__(cls, name, bases, new_attrs)

class MyClass(metaclass=RenameAttributesMeta):
    def __init__(self):
        self.__x = 1
        self.y = 2

obj = MyClass()

print(obj.__x_)

