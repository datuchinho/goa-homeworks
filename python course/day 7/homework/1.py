number = int(input())
divisors = [i for i in range(1, number + 1) if number % i == 0]
print(divisors)
