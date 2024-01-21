# Bankers roulette project.

import random
print("Welcome to a sample banker's roulette program!\n")
names=input("Please enter all the people's names \n"
           "seperated by a coma: \n\n")
fin=names.split(", ")
len=len(fin)
payer=random.randint(0,len-1)
payer_fin=fin[payer]
print(fin)
print("\n" + payer_fin + " will be settling the bill today!\n")
