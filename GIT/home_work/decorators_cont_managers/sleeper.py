from time import sleep

def Sleeper(seconds):
    def deco(func):
        def wrapper(*args, **kwargs):
            sleep(seconds)
            return func(*args, **kwargs)
        return wrapper
    return deco

@Sleeper(3)
def calc_somtng(a, b, c):
    return a + b + c

print(calc_somtng(1,2,3))