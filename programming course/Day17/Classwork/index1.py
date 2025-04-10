def manual_append(lst, item):
    lst[len(lst):] = [item]
    return lst

numbers = [1, 2, 3, 4, 5]
manual_append(numbers, 6)
print(numbers)
