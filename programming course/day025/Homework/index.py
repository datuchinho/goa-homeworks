def most_common_type(lst):
    type_counts = {}

    for item in lst:
        t = type(item)
        type_counts[t] = type_counts.get(t, 0) + 1

    most_common = max(type_counts, key=type_counts.get)
    return most_common

# მაგალითი:
data = [1, "hello", 2.5, 3, 4, "world", 5]
result = most_common_type(data)
print("ყველაზე ხშირი ტიპია:", result)
