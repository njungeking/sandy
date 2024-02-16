# First attempt at the Calculator project.

def add(num1,num2):
  return num1 + num2

def subtract(num1,num2):
  return num1 - num2

def multiply(num1,num2):
  return num1 * num2

def divide(num1,num2):
  return num1 / num2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide,
}

from art import logo
print(logo)

print("Welcome to a sample calculator program!\n")
num1 = int(input("Please enter the first number: \n"))
for sym in operations:
  print(sym)
oper = input("Please enter the operation that you wish: \n")
num2 = int(input("Please enter the second number: \n"))
desired_function = operations[oper]
ans = desired_function(num1,num2)
print(f"{num1} {oper} {num2} = {ans}")
