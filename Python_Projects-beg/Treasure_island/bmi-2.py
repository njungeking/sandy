# Nested conditional statements in
# a sample BMI calculator.

print("Welcome to a Body Mass Index calculator!\n")
weight=float(input("Please enter your weight in kilograms: \n"))
height=float(input("Please enter your height in metres: \n"))
bmi=weight/(height**2)
final=float("{:.1f}".format(bmi))
if final < 18.5:
  print(f"Your BMI is {final} and you are UNDERWEIGHT!\n")
elif final < 25:
  print(f"Your BMI is {final} and you have a NORMAL WEIGHT!\n")
elif final < 30:
  print(f"Your BMI is {final} and you are OVERWEIGHT!\n")
elif final < 35:
  print(f"Your BMI is {final} and you are OBESE!\n")
else:
  print(f"Your BMI is {final} and you are CLINICALLY OBESE!\n")
