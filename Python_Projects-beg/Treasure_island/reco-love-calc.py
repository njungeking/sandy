# A recap on the love calculator project.

print("Welcome to a love calculator project!\n")
name1=input("Please enter the first name: \n")
name2=input("Please enter the second name: \n")
lower1=name1.lower()
lower2=name2.lower()
names = lower1 + lower2
t=names.count("t")
r=names.count("r")
u=names.count("u")
e=names.count("e")
true=t+r+u+e
l=names.count("l")
o=names.count("o")
v=names.count("v")
e=names.count("e")
love=l+o+v+e
ans=int(str(true)+str(love))

if ans < 10 or ans > 90:
  print(f"Your score is {ans}, you go together like coke and mentos!\n")
elif ans > 40 and ans < 50:
  print(f"Your score is {ans}, you are alright together!\n")
else:
  print(f"Your score is {ans}!\n")
