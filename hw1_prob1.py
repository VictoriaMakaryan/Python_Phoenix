#problem 1 (input elements of the list and print the minimum)

ls = []
while len(ls) < 10:
    a = int(input("Enter a number"))
    ls.append(a)

min_el = ls[0]
for i in ls:
    if i < min_el:
        min_el = i
print(min_el)
