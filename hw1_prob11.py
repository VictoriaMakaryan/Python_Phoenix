#problem 11

num = int(input("Enter a number: "))

def palindrome(num):
    if str(num) == str(num)[::-1]:
        return True
    return False

def reverse(num):
    return int(str(num)[::-1])

def steps(num):
    step = 0
    while not palindrome(num):
        num = num + int(reverse(num))
        step += 1
    return step
print(steps(num))

