class Counter:
    count = 0

    def __init__(self) -> None:
        Counter.count += 1
        self.method_caller = 0

    def get_count(self):
        self.method_caller += 1
        return Counter.count
    
c1 = Counter()
c2 = Counter()

print(c1.get_count())
print(c1.method_caller)
