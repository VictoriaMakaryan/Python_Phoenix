#problem 5 (sort list that even elements are in the begining and odds are in the end)

ls = [1, 3, 2, 5, -23, 7, 12, -10, 9]

def func(ls):
    left = 0
    right = len(ls) - 1

    while left < right:
        while ls[left] % 2 == 0 and left < right:
            left += 1
        while ls[right] % 2 != 0 and left < right:
            right -= 1
        if left < right:
            ls[left], ls[right] = ls[right], ls[left]
    return ls

print(func(ls))
