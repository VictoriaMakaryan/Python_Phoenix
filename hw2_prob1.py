def divisors(n):
    return sum([i for i in range(1, n + 1) if n % i == 0])
print(divisors(10))
