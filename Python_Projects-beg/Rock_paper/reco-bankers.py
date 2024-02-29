# A recap of the Banker's roulette project.

import random
print("Welcome to a sample Banker's roulette program!\n")
peeps=input("Please enter the names of the people \n"
           "who have eaten today: \n")
names=peeps.split(", ")
len=len(names)
rand=random.randint(0, len-1)
payer=names[rand]
print(payer + " is going to pay for the bill today!\n")
