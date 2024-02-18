# A recap of the Calculator project.

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

def calc(): 
  print(logo)
  print("Welcome to a sample Calculator program!\n")
  num1 = int(input("Please enter the first number: "))
  cont = True
  while cont:
    for sym in operations:
      print(sym)
    oper = input("Please choose the operation that you wish to perform: ")
    num2 = int(input("Pleae enter the next number: "))
    func = operations[oper]
    ans = func(num1,num2)
    print(f"{num1} {oper} {num2} = {ans}")
    again = input(f"Would you like to continue with {ans}? 'y' or 'n'? ")
    if again == 'n':
      print("Goodbye!")
      cont = False
      calc()
    elif again == "y":
      num1 = ans
calc()
