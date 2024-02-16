# A second attempt involving a third number in the Calculator project.

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
cont = input(f"Would you like to continue with {ans}? 'yes' or 'no'? ")
if cont == "yes":
  oper_two = input("Please enter the operation that you wish to use: ")
else:
  print("Goodbye!")
num3 = int(input("Please enter the third number: "))
des_func_two = operations[oper_two]
ans_two = des_func_two(ans,num3)
print(f"{ans} {oper_two} {num3} = {ans_two}")
