class IterRange:
    def __init__(self, start, end, step) -> None:
        self.start = start
        self.end = end
        self.step = step
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.start >= self.end:
            raise StopIteration
        res = self.start
        self.start += self.step
        return res
    
check = IterRange(1, 10, 2)
for i in check:
    print(i)