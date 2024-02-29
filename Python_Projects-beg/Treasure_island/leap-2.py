# Leap year determination using
# nested conditional statements.

print("Welcome to a Leap year checking program!\n")
year=int(input("Please enter the year that you wish to check: \n"))
if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print(f"The year {year} is A Leap year!\n")
    else:
      print(f"The year {year} is NOT a Leap year!\n")
  else:
    print(f"The year {year} is A Leap year!\n")
else:
  print(f"The year {year} is NOT a Leap year!\n")
