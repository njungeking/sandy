# For loops in a student height mean calculator project.

print("Welcome to a mean student height calculator!\n")
student_heights=input("Please put the respective heights of \n"
            "the students: \n").split()
for x in range(0,len(student_heights)):
  student_heights[x]=int(student_heights[x])
print(student_heights)

sum_heights = 0
for height in student_heights:
  sum_heights += height
print(sum_heights)

num_stu = 0
for num in student_heights:
  num_stu += 1
print(num_stu)

mean=round(sum_heights/num_stu)
print(f"The average height of the students is: {mean}!\n")
