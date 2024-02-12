# A second attempt at the student grades project.

student_scores = {
  "Harry": 91,
  "Ron": 90,
  "Hermoine": 80,
  "Draco": 70,
  "Neville": 62,
}

print("Welcome to a student grades program!\n")

student_grades = {}

for student in student_scores:
  student_scores[student]
  if student_scores[student] > 90 and student_scores[student] < 101:
    student_scores[student] = "Outstanding"
  elif student_scores[student] > 80:
    student_scores[student] = "Exceeds Expectations"
  elif student_scores[student] > 70:
    student_scores[student] = "Acceptable"
  elif student_scores[student] < 71:
    student_scores[student] = "Fail"
  student_grades = student_scores

print(student_grades)
