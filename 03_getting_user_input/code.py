while(True):
    user_age = input("How old are you? ")
    try:
        years = int(user_age)
        seconds = years * 365 * 24 * 60 * 60
        print(f"You are {seconds} seconds old")
        break
    except ValueError:
        print("Please input an integer")
