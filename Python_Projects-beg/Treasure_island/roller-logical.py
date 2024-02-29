# Roller-coaster ticketing project
# using logical operators.

print("Welcome to a roller-coaster ticketing program!\n")
height = int(input("Please enter your height in centimeters: \n"))
bill = 0
if height >= 120:
    print("You are welcome to take the ride!\n")
    age = int(input("How old are you? \n"))
    if age <= 12:
        bill += 10
        print("The cost of your ticket is $10.\n")
    elif age < 18:
        bill += 13
        print("The cost of your ticket is $13.\n")
    elif age >= 45 and age <= 55:
        bill = 0
        print("The cost of your ticket is $0.\n")
    else:
        bill += 20
        print("The cost of your ticket is $20.\n")

    photo = input("Would you like to take a photo while \n"
                  "on the roller-coaster? 'Y' or 'N': \n")
    if photo == 'Y':
        if age >= 45 and age <= 55:
            bill = 0
            print(f"The final cost of your ticket is ${bill}!\n")
        else:
            bill += 3
            print(f"The final cost of your ticket is ${bill}!\n")
    elif photo == 'N':
        print(f"The final cost of your ticket is ${bill}!\n")

else:
    print("Sorry. You cannot take this ride!\n")
