# Multiple if statements in succession
# in a roller-coaster ticketing project.

print("Welcome to a roller-coaster ticketing program!\n")
height=int(input("Please enter your height in centimetres: \n"))
bill = 0
if height >= 120:
  print("You are welcome to take a ride!\n")
  age=int(input("How old are you: \n"))
  if age <= 12:
    bill = 5
    print("The ticket is $5.\n")
  elif age < 18:
    bill = 7
    print("The ticket is $7.\n")
  else:
    bill = 15
    print("The ticket is $15.\n")

  photo = input("Would you like a photo? Type 'Y' or 'N': \n")
  if photo == 'Y':
    bill += 3

  print(f"Your final ticket-price is ${bill}!\n")

else:
  print("Sorry. You are not welcome to take a ride!\n")
