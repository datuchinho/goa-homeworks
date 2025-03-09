number = int(input("Enter a number between 1 and 50: "))

if 1 <= number <= 50:
    for i in range(number, 101, number):
        print(i)
else:
    print("ricxvi ar aris 1 da 50 shoris.")