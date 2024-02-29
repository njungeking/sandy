# Nested conditional statements.

print("Welcome to a roller-coaster ticketing program!\n")
height=int(input("What is your height in centimeters: \n"))
if height >= 120:
  print("You are alllowed to ride the roller-coaster!\n")
  age=int(input("How old are you? \n"))
  if age <= 12:
    print("Please deposit $50.\n")
  elif age < 18:
    print("Please deposit $120.\n")
  else:
    print("Please deposit $200.\n")
else:
  print("Sorry. You are not allowed to ride this roller-coaster!\n")
