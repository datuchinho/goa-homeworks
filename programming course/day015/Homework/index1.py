def even_sum_odd_count(lst):
    even_sum = sum(x for x in lst if x % 2 == 0)
    odd_count = sum(1 for x in lst if x % 2 != 0)
    return even_sum, odd_count

lst = [1, 4, 3, 6, 9, 11, 17, 13, 26, 30]
result = even_sum_odd_count(lst)
print(result)
