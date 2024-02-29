# Addition of a recall property to the Calculator project.

from art import logo

def add(num1,num2):
  return num1 + num2

def subtract(num1,num2):
  return num1 - num2

def multiply(num1,num2):
  return num1 * num2

def divide(num1,num2):
  return num1 / num2

def calc():
    
  print(logo)
  operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
  }
  print("Welcome to a sample calculator program!\n")
  num1 = int(input("Please enter the first number: "))
  for sym in operations:
    print(sym)
  
  proceed = True
  while proceed:
      
    oper = input("Please enter the operation that you would like to perform: ")
    func = operations[oper]
    num2 = int(input("Please enter the next number: "))
    ans = func(num1,num2)
    print(f"{num1} {oper} {num2} = {ans}")
    cont = input(f"Do you wish to continue with {ans}? 'y' or 'n': ")
    if cont == "y":
      num1 = ans
    else:
      proceed = False
      print("Goodbye!")
      calc()

calc()
