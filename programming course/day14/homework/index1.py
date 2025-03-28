num = int(input("enter number:"))

if num % 2 == 0:
    num += 5
else:
    num *= 3

res = num % 5

print(res)