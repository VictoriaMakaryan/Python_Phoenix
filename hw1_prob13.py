#problem 13 (recurssive function to return sum of digits of a number)

num = 12345
def func(num):
    if num == 0:
        return 0
    return num % 10 + func(num // 10)
print(func(num))
