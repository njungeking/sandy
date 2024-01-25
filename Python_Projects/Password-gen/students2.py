  # For loops in a mean height calculator project.

print("Welcome to a mean height calculator program!\n")
student_heights=input("Please enter the respective student heights "
                     "in cm: \n").split()
for n in range(0,len(student_heights)):
  student_heights[n]=int(student_heights[n])
print(student_heights)

sum_heights=0
for height in student_heights:
  sum_heights += height
print(sum_heights)

num_stu=0
for num in student_heights:
  num_stu += 1
print(num_stu)

mean=round(sum_heights/num_stu)
print(f"The average height is {mean}!\n")
