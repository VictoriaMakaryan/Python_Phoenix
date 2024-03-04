#problem 9 (print first and fourth rows min and max elements sum)

import random
a = 5
ls = [[random.randint(1, 10) for _ in range(a)] for _ in range(a)]
print(ls)
max_el = ls[0][0]
min_el = ls[0][0]

for row in ls[1::2]:
    for elem in row: 
        if elem < min_el:
            min_el = elem
        if elem > max_el:
            max_el = elem

print(max_el + min_el) 