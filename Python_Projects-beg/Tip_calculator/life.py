# A life in weeks project.
# Calculation of the time left in years, months
# weeks and days until the age of 90 years.

print("Welcome to a life in weeks program!\n")
age=input("What is your current age: \n")
years=90-int(age)
months=years*12
weeks=years*52
days=years*365
print(f"You have {years} years, {months} months, {weeks} weeks \n"
      f"and {days} days left until 90 years!\n")
