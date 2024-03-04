#problem 15 (itarative function to count gcd of 2 numbers)

def gcd(num1, num2):
    if num1 != 0 and num2 != 0:
        if num1 % num2 == 0:
            return num2
        while num1 % num2 != 0:
            num1, num2 = num2, num1 % num2
        return num2
    else:
        return "Enter non-zero numbers"
print(gcd(0, 0))
