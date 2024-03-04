#problem 2 (print the odd numbers of the list)

ls = [1, 3, 2, 5, 23, 7, 12, 10, 9]
count = 0
print(ls)
for i in range(len(ls)):
    if ls[i] % 2 != 0:
        count += 1
print(count)
