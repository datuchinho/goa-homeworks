paroli = int(input("sheiyyvanet paroli: "))

if paroli > 1:
    for i in range(2, int(num1 ** 0.5) + 1):
        if paroli  % i == 0:
            print("paroli ar aris swori")
            break
    else:
        print("parli sworia")
else:
    print("paroli sworia")
