# Leap Year determination using
# conditional statements.

year=int(input("Which year do you want to check? \n"))
if year % 4 == 0:
  if year % 100 != 0:
    print("A leap year!\n")
  elif year % 100 == 0 and year % 400 == 0:
    print("A leap year!\n")
  else:
    print("NOT a leap year!\n")
else:
  print("NOT a leap year!\n")
