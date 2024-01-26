# For loops in student scores project.

print("Welcome to a highest student scores determiner!\n")
scores=input("Please enter the respective student scores: \n").split()
for x in range(0,len(scores)):
  scores[x]=int(scores[x])
print(scores)

highest = 0
for marks in scores:
  if marks > highest:
    highest = marks
print(f"The highest score is: {highest}!\n")
