# Pizza ordering program project.

print("Welcome to a Pizza Ordering program!\n")
size = input("What size of pizza do you want? 'S', 'M' or 'L'? \n")
pepperoni = input("Do you want pepperoni? 'Y' or 'N': \n")
cheese = input("Do you want extra cheese? 'Y' or 'N': \n")
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
