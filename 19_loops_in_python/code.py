# improved game 'guess the number'
from secrets import randbelow
secret_number = randbelow(100) + 1
user_input = input("Do you want to play? (Y/n) ")

while user_input != 'n':
    user_input = input("Guess the number ('n' to end the game) ")
    try:
        user_number = int(user_input)
        while user_number != secret_number:
            if user_number > secret_number:
                user_input = input("Try smaller number ('n' to end the game) ")
                user_number = int(user_input)
            else:
                user_input = input("Try bigger number ('n' to end the game) ")
                user_number = int(user_input)
        print("Correct!")
        break
    except ValueError:
        if user_input == 'n':
            break
        else:
            print("Please input an integer or 'n' to end the game")
print("Have a nice day!")
