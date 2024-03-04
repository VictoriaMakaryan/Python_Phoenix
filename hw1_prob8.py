#problem 8 (make a NxN matricx and print the first and third columns)

import random
a = 5
ls = [[i for i in range(a)] for i in range(a)]

for i in range(len(ls)):
    print(ls[i][1:4:2])
