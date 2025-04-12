def manual_remove(lst, value):
    result = []
    removed = False
    for item in lst:
        if item == value and not removed:
            removed = True
            continue
        result.append(item)
    return result

def manual_index(lst, value):
    for i in range(len(lst)):
        if lst[i] == value:
            return i
    raise ValueError("Value not found")

def manual_len(lst):
    count = 0
    for _ in lst:
        count += 1
    return count

def manual_pop(lst):
    if manual_len(lst) == 0:
        raise IndexError("pop from empty list")
    result = []
    for i in range(manual_len(lst) - 1):
        result.append(lst[i])
    return result, lst[-1]

def manual_reverse(lst):
    result = []
    for i in range(manual_len(lst)-1, -1, -1):
        result.append(lst[i])
    return result
