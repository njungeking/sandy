# A Tip Calculator project.

print("Welcome to a Tip-Calculator program!\n")
bill=input("What is the total bill? \n$")
tip=input("What percentage tip would you like \n"
         "to give? 10, 12 or 15? \n")
people=input("How many people are to split this bill? \n")
final=(float(bill)*(1+int(tip)/100))/int(people)
ans="{:.2f}".format(final)
print(f"Each person should pay: ${ans}!\n")
