# Yet another recap of the pizza
# ordering program project.

print("Welcome to a pizza ordering program!\n")
size=input("Please select the size of pizza that \n"
          "you wish to purchase: 'S', 'M' or 'L': \n")
pepperoni=input("Would you like some pepperoni with \n"
               "your pizza? 'Y' or 'N': \n")
cheese=input("Would you like some extra cheese on \n"
            "your pizza? 'Y' or 'N': \n")
bill = 0
if size == 'S':
  bill += 15
elif size == 'M':
  bill += 20
elif size == 'L':
  bill += 25

if pepperoni == 'Y':
  if size == 'S':
    bill += 2
  else:
    bill += 3

if cheese == 'Y':
  bill += 1

print(f"The final cost of your pizza is ${bill}!\n")
