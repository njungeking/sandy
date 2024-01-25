# For loops in mean calculator.

print("Welcome to an average student height calculator!\n")
student_heights=input("Input a list of student heights: \n").split()
for n in range(0,len(student_heights)):
  student_heights[n] = int(student_heights[n])
print(student_heights)

sum_heights=0
for heights in student_heights:
  sum_heights += heights
print(sum_heights)

num_students=0
for num in student_heights:
  num_students += 1
print(num_students)

mean=round(sum_heights/num_students)
print(f"The average height is: {mean}")
