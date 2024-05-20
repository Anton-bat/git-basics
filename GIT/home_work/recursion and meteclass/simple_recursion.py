def recursive_sum(n):
    if n <= 0:
        return 0
    else:
        return n % 10 + recursive_sum(n // 10)


result = recursive_sum(1234)
print(result)  