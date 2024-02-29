# Another even number summation project
# using the range function from 0-100.

print("Welcome to an even number summation program!\n")

total=0
for x in range(0,101,2):
  total+=x
print(f"The total of the even numbers between 0 and 100 is: {total}!\n")
