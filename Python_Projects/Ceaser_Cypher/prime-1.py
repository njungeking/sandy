# Prime number checker project.

def primer(num):
  prime = True
  for i in range(2,num):
    if num % i == 0:
      prime = False
  if prime:
    print(f"{num} is a Prime number!\n")
  else:
    print(f"{num} is not a Prime number!\n")

print("Welcome to a prime number checking program!\n")
n = int(input("Please enter the number that you wish to check?\n"))
primer(num=n)
