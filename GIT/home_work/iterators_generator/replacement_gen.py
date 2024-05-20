def permutations(lst):
    if len(lst) == 0:
        yield []
    elif len(lst) == 1:
        yield lst
    else:
        for i in range(len(lst)):
            for char in permutations(lst[:i] + lst[i+1:]):
                yield [lst[i]] + char



for char in permutations([1, 2, 3]):
    print(char)
        

