# A recap of the prime number checker project.

def primer(number):
  prime = True
  for i in range(2,number):
    if number % i == 0:
      prime = False
  if prime:
    print(f"{number} is a PRIME NUMBER!\n")
  else:
    print(f"{number} is NOT A PRIME NUMBER!\n")

print("Welcome to a Prime number checking program!\n")
n = int(input("Please enter the number that you wish to check: \n"))
primer(number=n)
