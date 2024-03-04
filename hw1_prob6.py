#problem 6 (return new list with odd indexes)

ls = [1, 3, 2, 5, -23, 7, 12, -10, 9]
ls_new = []
def odd(ls):
    for i in range(len(ls)):
        if i % 2 != 0:
            ls_new.append(ls[i])
    return ls_new
print(odd(ls))
