num = int(input("Enter a number between 1 and 50: "))

if 1 <= num <= 50:
    for i in range(num, 101, num):
        print(i)
else:
    print("ricxvi ar aris 1 da 50 shoris.")