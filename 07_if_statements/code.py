day_of_week = input("What day of week is today? ").lower()

if day_of_week == "saturday":
    print("Yay! Weekend starts!")
elif day_of_week == "sunday":
    print("Oh no! Weekend ends")
else:
    print("Go to work!")