num1 = int(input("შეიყვანე პირველი რიცხვი: "))
num2 = int(input("შეიყვანე მეორე რიცხვი: "))
num3 = int(input("შეიყვანე მესამე რიცხვი: "))

if num1 >= num2 and num1 >= num3:
    print("ყველაზე დიდი რიცხვია:", num1)
elif num2 >= num1 and num2 >= num3:
    print("ყველაზე დიდი რიცხვია:", num2)
else:
    print("ყველაზე დიდი რიცხვია:", num3)
