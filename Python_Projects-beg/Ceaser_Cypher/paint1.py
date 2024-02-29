# Paint can calculator project.

import math
print("Welcome to a Paint-can calculator program!\n")

def paint_calc(cover,height,width):
  paint = (height * width)/cover
  print(math.ceil(paint))

test_h = int(input("Height of the wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
