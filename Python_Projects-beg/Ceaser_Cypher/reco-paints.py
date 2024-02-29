# A recap of the Paint cans project.

import math
def paint_calc(cover, width, height):
  cans = (width * height)/cover
  cans_final=math.ceil(cans)
  print(f"You will need {cans_final} for this project!")

print("Welcome to a paint cans calculator!\n")
test_h = int(input("Height of the wall: "))
test_w = int(input("Width of the wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
