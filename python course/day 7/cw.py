text = input("Sheiyvaanet sityva: ")
num = int(input("enter number: "))
print(text[num - 1])

#2

for i in range (100,0,-1):
    print(i)


#3

for i in range(0,100):
    if i % 2 != 0:
        print(i)


#4

for i in range(250,490,10):
    print(i)

#5

word = input("შეიყვანეთ სიტყვა: ")

if word.startswith("D"):
    print(True)
else:
    print(False)