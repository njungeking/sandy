# Addition of the even numbers project
# using the range function from 0-100.

print("Welcome to an even numbers addition program!\n")

total=0
for num in range(0,101,2):
  total += num
print(f"The sum total of the even numbers is {total}!\n")
