secret_number = 5678
print("Guess the four-digit number!")

while True:
    try:
        guess = int(input("Enter your guess: "))
        
        if guess < 1000 or guess > 9999:
            print("sheiyvanet 4 nishna ricxvi.")
            continue
        
        if guess == secret_number:
            print("gilocavt sworia! 🎉")
            break
        elif guess < secret_number:
            print("dabalia scadet ufro magali! ricxvi")
        else:
            print("magalia scadet ufro dabali ricxvi!")
        
    except ValueError:
        print("Please enter a valid number.")
