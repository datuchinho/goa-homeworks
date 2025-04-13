num = int(input("Enter a number: "))

if num > 1:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            print("Your number is not a prime")
            break
    else:
        print("Your number is a prime")
else:
    print("Your number is not a prime")
