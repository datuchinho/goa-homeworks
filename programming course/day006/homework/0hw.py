num = int(input("Enter a number: "))
odd_sum = 0

for i in range(1, num + 1, 2):
    odd_sum += i

print("Sum of odd numbers:", odd_sum)
