# A love calculator project.

print("Welcome to a love calculator program!\n")
name1=input("Please enter the first name: \n")
name2=input("Please enter the second name: \n")
lower1=name1.lower()
lower2=name2.lower()
t=lower1.count("t") + lower2.count("t")
r=lower1.count("r") + lower2.count("r")
u=lower1.count("u") + lower2.count("u")
e=lower1.count("e") + lower2.count("e")
dig1=t+r+u+e
l=lower1.count("l") + lower2.count("l")
o=lower1.count("o") + lower2.count("o")
v=lower1.count("v") + lower2.count("v")
e=lower1.count("e") + lower2.count("e")
dig2=l+o+v+e
ans=int(f"{dig1}{dig2}")

if ans < 10 or ans > 90:
  print(f"Your score is, {ans} and you go together like coke and mentos!\n")
elif ans > 40 and ans < 50:
  print(f"Your score is, {ans} and you are alright together!\n")
else:
  print(f"Your score is {ans}!\n")
