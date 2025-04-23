def remove_odd_elements(arr):
    return [item for item in arr if item % 2 == 0]

arr = [1, 2, 3, 4, 5, 6]
print(remove_odd_elements(arr))
