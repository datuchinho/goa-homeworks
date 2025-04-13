while True:
    word = input("Enter a 3-letter word: ")
    
    if len(word) != 3:
        print("Please enter exactly three letters.")
    else:
        print(word == word[::-1])
        break
