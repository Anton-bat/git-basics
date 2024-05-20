class CyclicIterator:
    def __init__(self, iterable):
        self.iterable = iterable
        self.iterator = iter(iterable)
        self.peaked = None

    def __iter__(self):
        return self

    def __next__(self):
        if self.peaked is not None:
            res = self.peaked
            self.peaked = None
            return res
        try:
            return next(self.iterator)
        except StopIteration:
                self.iterator = iter(self.iterable)

    def peak(self):
        if self.peaked is None:
             self.peaked = next(self.iterator)
        return self.peaked
    


cyclic_iter = CyclicIterator([1, 2, 3])

print(next(cyclic_iter))
print(cyclic_iter.peak())
print(next(cyclic_iter))