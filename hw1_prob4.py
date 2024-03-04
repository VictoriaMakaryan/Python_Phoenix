#problem 4 (input list elements and print sum of max and min)

ls = [1, 3, 2, 5, -23, 7, 12, -10, 9]
max_el = ls[0]
min_el = ls[0]
for i in ls:
    if max_el < i:
        max_el = i
    if min_el > i:
        min_el = i
print(max_el + min_el)
