#problem 12 (return the binary representation of the givenn decimal)

num = int(input("Enter a number: "))
s = ""

while num > 0:
    a = num % 2
    s = str(a) + s
    num = num // 2

if num == 0:
    s = str(0) + s

print(s)
