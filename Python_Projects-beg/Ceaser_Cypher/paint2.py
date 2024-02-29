# Attempt #2 on the Paint cans project.

import math

print("Welcome to a paint can calculator!\n")

def paint_calc(cover, height, width):
  cans = (height * width)/cover
  int_cans = math.ceil(cans)
  print(f"You will need {int_cans} cans!")

test_h = int(input("Height of the wall: "))
test_w = int(input("Width of the wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
