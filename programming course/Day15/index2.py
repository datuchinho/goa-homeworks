my_list = [1, 2, 3, 4, 6, 8, 9]
for i in range(1, len(my_list)):
    while my_list[i] != my_list[i-1] + 1:
        my_list.insert(i, my_list[i-1] + 1)
        i += 1

print(my_list)
