student_scores = {
  "Harry": 81,
  "Mwenje": 78,
  "Oscar": 99,
  "Olipo": 74,
  "Gronk": 62
}

student_grades = {}
for student in student_scores:
  if student_scores[student] > 89 and student_scores[student] < 101:
    student_scores[student] = "Outstanding"
  elif student_scores[student] > 80:
    student_scores[student] = "Exceeds Expectations"
  elif student_scores[student] > 70:
    student_scores[student] = "Acceptable"
  elif student_scores[student] < 69:
    student_scores[student] = "Fail"
student_grades = student_scores
print(student_grades)
