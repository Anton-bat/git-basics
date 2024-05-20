class FilterIter():
    def __init__(self, iterat, func) -> None:
        self.iterat = iterat
        self.func = func
        self.iterator = iter(iterat)

    def __iter__(self):
        return self
    
    def __next__(self):
        while True:
            value = next(self.iterator)
            if self.func(value):
                return value

f_iter = FilterIter([1, 2, 3, 4], lambda x: x % 2 == 0)

while True:
    try:
        print(next(f_iter))
    except StopIteration:
        break