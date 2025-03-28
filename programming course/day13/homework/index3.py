number = int(input())
digit_sum = sum(int(digit) for digit in str(number))
print(number % digit_sum)
