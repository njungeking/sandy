# Another go at randomisation.

import random

print("Welcome to a virtual coin toss game!\n")
ans = random.randint(0, 1)
if ans == 1:
    print("Heads!\n")
else:
    print("Tails!\n")

