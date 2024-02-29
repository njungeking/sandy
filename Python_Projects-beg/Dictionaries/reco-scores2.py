# A second recap attempt of the student_scores project.

student_scores = {
"Matilde": 89,
"Daisy": 65,
"Peter": 82,
"Violet": 33,
"Paul": 80,
"Sam": 97,
}

print("Welcome to a Students' grades project!\n")
student_grades = {}

for student in student_scores:
  marks = student_scores[student]
  if marks > 90 and marks < 101:
    student_grades[student] = "Excellent. Goodjob!"
  elif marks > 80:
    student_grades[student] = "Well done."
  elif marks > 70:
    student_grades[student] = "Fair enough."
  elif marks > 60:
    student_grades[student] = "Pass."
  elif marks < 61:
    student_grades[student] = "Fail!"

print(student_scores)
print(student_grades)
