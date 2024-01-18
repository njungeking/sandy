# A pizza ordering program project.

print("Welcome to a pizza ordering program!\n")
size=input("Please select the size of the pizza \n"
          "that you wish to buy: 'S', 'M' or 'L': \n")
pepperoni=input("Would you like to add some pepperoni? \n"
               "'Y' or 'N'? \n")
cheese=input("Would you like to add some extra cheese? \n"
            "'Y' or 'N'? \n")
bill = 0
if size == 'S':
  bill += 15
  if pepperoni == 'Y':
    bill += 2
elif size == 'M':
  bill += 20
  if pepperoni == 'Y':
    bill += 3
elif size == 'L':
  bill += 25
  if pepperoni == 'Y':
    bill += 3

if cheese == 'Y':
  bill += 1
  print(f"The final bill for your pizza is ${bill}!\n")
else:
  print(f"The final bill for your pizza is ${bill}!\n")
