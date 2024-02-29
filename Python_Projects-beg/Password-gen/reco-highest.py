# A recap on the highest students' scrore project.

print("Welcome to a highest score determinant program!\n")
scores=input("Please enter the respective student scores: \n").split()
for x in range(0,len(scores)):
  scores[x]=int(scores[x])
print(scores)

highest = 0
for mark in scores:
  if mark > highest:
    highest = mark
print(f"The highest score is {highest}!\n")
