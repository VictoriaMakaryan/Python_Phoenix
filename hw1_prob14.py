#problem 14 (recurrsive function to count the greatest comman divisor of 2 numbers)

def gcd(num1, num2):
    if num1 % num2 == 0:
        return num2
    return gcd(num2, num1 % num2)
print(gcd(12, 16))
