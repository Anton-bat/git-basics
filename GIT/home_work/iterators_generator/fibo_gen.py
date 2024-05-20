def fibo_gen(number):
        a, b = 0, 1
        yield a
        while b <= number:
                yield b 
                a, b = b, a + b 

for i in fibo_gen(100):
        print(i, end=",")