def func(n):
    dict = {}
    for i in range(n + 1):
        dict[i] = i ** 3
    return dict
print(func(5))