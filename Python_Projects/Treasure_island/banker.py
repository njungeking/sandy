# Banker's roulette project.

import random
print("Welcome to a random payer program!\n")
name_str=input("Please enter everybody's name seperated by \n"
              "a coma: \n")
names=name_str.split(", ")
print(names)
payer=random.randint(0,3)
print(f"Today's bill will be paid by: {names[payer]}!")
