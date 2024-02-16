# A second attempt at the Calculator project.

def add(num1,num2):
  return num1 + num2

def subtract(num1,num2):
  return num1 - num2

def multiply(num1,num2):
  return num1 * num2

def divide(num1,num2):
  return num1 / num2

from art import logo
print (logo)
print("Welcome to a sample calculator project!\n")
operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide,
}
num1 = int(input("Please enter the first number: "))
for sym in operations:
  print(sym)
oper = input("Please enter the operation that you wish to use: ")
num2 = int(input("Please enter the second number: "))
des_func = operations[oper]
ans = des_func(num1,num2)
print(f"{num1} {oper} {num2} = {ans}")
