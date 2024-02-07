# Prime number checker project #2.

def primer(num):
  prime = True
  for i in range(2,num):
    if num % i == 0:
      prime = False
  if prime:
    print(f"The number: {num} is A Prime number!\n")
  else:
    print(f"The number: {num} is NOT a Prime number!\n")

print("Welcome to a prime number checking program!\n")
n = int(input("Please enter the number that you "
"wish to check: \n"))
primer(num=n)
