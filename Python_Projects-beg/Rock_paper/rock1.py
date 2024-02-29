rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Rock, Paper and Scissors game project.

import random
user=int(input("What do you choose? \n"
"Type 0 for Rock, 1 for Paper or 2 for Scissors.\n\n"))
ans=[rock,paper,scissors]
user_choice=ans[user]
print("\nYou chose: ")
print(user_choice)

print("\nComputer chose: \n")
comp=random.randint(0,2)
comp_choice=ans[comp]
print(comp_choice)

if user == comp:
  print("It is a Draw!")
elif user == 0 and comp == 2:
  print("You win!\n")
elif user == 0 and comp == 1:
  print("You lose!\n")
elif user == 1 and comp == 0:
  print("You win!\n")
elif user == 1 and comp == 2:
  print("You lose!\n")
elif user == 2 and comp == 0:
  print("You lose!\n")
elif user == 2 and comp == 1:
  print("You win!\n")
