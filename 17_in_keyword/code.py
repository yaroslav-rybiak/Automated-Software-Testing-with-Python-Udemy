#game 'guess the number'
secret_number = 42
user_input = input("Do you want to play? ").lower()
if user_input in ("y", "yes"):
    while True:
        try:
            user_number = int(input("Guess the number "))
            while user_number != secret_number:
                user_number = int(input("No! Guess again "))
            print("Correct!")
            break
        except ValueError:
            print("Please input an integer")

else:
    print("Have a nice day!")
