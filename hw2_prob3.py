def pythagoras(n):
    return [(i, j, n) for i in range(1, n + 1) for j in range(1, n + 1) if i ** 2 + j ** 2 == n ** 2 and i < n and j < n]
print(pythagoras(13))