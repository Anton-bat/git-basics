
def typechecker(*types):
    def deco(func):
        def wrapper(*args, **kwargs):
            for arg, arg_type in zip(args, types):
                if not isinstance(arg, arg_type):
                    raise TypeError(f"(given {arg} is not suitable with {arg_type.__name__})")
                return func(*args, **kwargs)
        return wrapper
    return deco
    
@typechecker(int, str)
def do_something(a, b, c):
    return a + len(b) + len(c)

print(do_something(10, "Does", "matter"))

