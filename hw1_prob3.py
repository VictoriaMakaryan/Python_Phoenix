#problem 3 (return the list without the element under the given index)

def remove_item(ls, i):
    ls.remove(ls[i])
    return ls
ls = [1, 3, 2, 5, 23, 7, 12, 10, 9]
i = 5
print(remove_item(ls, i))
