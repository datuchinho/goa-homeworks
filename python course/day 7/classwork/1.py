text = input("Enter a text: ")
num = int(input("Enter a number: "))

print(text[num] if 0 <= num < len(text) else "Invalid number")
