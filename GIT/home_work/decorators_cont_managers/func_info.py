
def func_info(func):

    def inner(*args, **kwargs):
        print(f'{func.__name__} is been called with params: {args}') 
        res = func(*args, **kwargs)
        print(f'{func.__name__} returned this value: {res}') 
        return res
    return inner


@func_info
def calc_something(a, b, c):
    return a + b + c


calc_something(1,3,5)
