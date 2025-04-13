def divisible_numbers(lst, num):
    result = []
    for x in lst:
        if x % num == 0:
            result.append(x)
    return result

lst = [1, 23, 165, 2, 3, 92, 10, 34, 911]
num = 3
print(divisible_numbers(lst, num))
