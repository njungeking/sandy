# A recap #1 of the student scores project.

student_scores = {
"Oscar": 89,
"Piomonte": 99,
"Marybeth": 54,
"Peter": 44,
"Evans": 78,
}

print("Welcome to a student scores grades program!\n")
student_grades = {}

for student in student_scores:
  marks = student_scores[student]
  if marks > 90 and marks < 100:
    student_grades[student] = "Excellent"
  elif marks > 80:
    student_grades[student] = "Good"
  elif marks > 70:
    student_grades[student] = "Fair Enough"
  elif marks < 71:
    student_grades[student] = "Fail"

print(student_scores)
print(student_grades)
