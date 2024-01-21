# Bankers roulette project.

import random
print("Welcome to a sample Banker's roulette program!\n")
inp=input("Please enter all the people's names \n"
         "seperated by a coma and space: \n")
names=inp.split(", ")
print(names)
len=len(names)
rand=random.randint(0, len-1)
payer=names[rand]
print(f"\nToday's bill will be settled by {payer}!\n")
