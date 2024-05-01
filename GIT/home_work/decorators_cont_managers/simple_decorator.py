def just_deco(func):

    def inner(*args, **kwargs):  
        res = func(*args, **kwargs)
        return res
    return inner

@just_deco
def first_m():
    return "Some func used"

@just_deco
def calc_something(a, b, c):
    return f"\n{a * b * c}"

@just_deco
def second_m():
    return "\nSome func used"

print(first_m(), calc_something(1,3,5), second_m())
