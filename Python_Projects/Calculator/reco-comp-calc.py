from art import logo

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

def calc():
    
  print(logo)
  print("Welcome to a sample calculator program!\n")
  num1 = float(input("Please enter the first number: "))
  
  cont = True
  while cont:
      
    for sym in operations:
      print(sym)
    oper = input("Which operation would you like to use: ")
    num2 = float(input("Please enter the next number: "))
    func = operations[oper]
    ans = func(num1,num2)
    print(f"{num1} {oper} {num2} = {ans}")
    proc = input(f"Would you like to proceed with: {ans}? 'y' or 'n': ")
    if proc == 'n':
      print("Goodbye!")
      cont = False
      calc()
    elif proc == 'y':
      num1 = ans
calc()
