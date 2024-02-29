# An odd or even number checker project.

print("Welcome to an odd or even number checker.\n")
number=int(input("Please enter the number that you wish to check: \n"))
if number % 2 == 0:
  print(f"The number: {number}, is an EVEN number!\n")
else:
  print(f"The number: {number}, is an ODD number!\n")
