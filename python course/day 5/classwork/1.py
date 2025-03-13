correct_password = "mySecretPassword"

while True:
    entered_password = input("Enter your password: ")
    if entered_password == correct_password:
        print("Password is correct!")
        break
    else:
        print("Incorrect password. Try again.")
