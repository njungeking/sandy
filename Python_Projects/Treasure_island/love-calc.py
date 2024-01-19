# A love calculator project.

print("Welcome to a love calculator program!\n")
name1=input("Please enter the first name: \n")
name2=input("Please enter the second name: \n")
lower_name1=name1.lower()
lower_name2=name2.lower()
t=lower_name1.count("t") + lower_name2.count("t")
r=lower_name1.count("r") + lower_name2.count("r")
u=lower_name1.count("u") + lower_name2.count("u")
e=lower_name1.count("e") + lower_name2.count("e")
dig1=t+r+u+e
l=lower_name1.count("l") + lower_name2.count("l")
o=lower_name1.count("o") + lower_name2.count("o")
v=lower_name1.count("v") + lower_name2.count("v")
e=lower_name1.count("e") + lower_name2.count("e")
dig2=l+o+v+e
ans=int(f"{dig1}{dig2}")

if ans < 10 and ans > 90:
  print(f"Your score is {ans}, you go together like coke and mentos!\n")
elif ans > 40 and ans < 50:
  print(f"Your score is {ans}, you are alright together!\n")
else:
  print(f"Your score is {ans}!\n")
