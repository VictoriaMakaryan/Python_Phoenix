#problem 10 (implement pop function)

ls = [1, 2, 3, 4, 5]

def pop_func(ls):
    return ls[:len(ls) - 1]

print(pop_func(ls))
