my_list = [1, 2, 3, 3, 4, 5]

for i in range(1, len(my_list)):
    if my_list[i] != my_list[i-1] + 1:
        my_list.pop(i)
        break

print(my_list)
