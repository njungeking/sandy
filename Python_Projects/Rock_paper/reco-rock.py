import random

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

# A recap of the rock, paper, scissors project.

print("Welcome to a rock, paper and scissors game!\n")
user=int(input("Type 0 for rock, 1 for paper and 2 for scissors: \n"))
list=[rock,paper,scissors]
if user > 2:
  print("You have entered a wrong value. Restart the game!\n")
else:
  user_choice=list[user]
  print("You have chosen: ")
  print(user_choice)

  comp=random.randint(0,2)
  comp_choice=list[comp]
  print("Computer chose: \n")
  print(comp_choice)

  if user == comp:
    print("It is a draw")
  elif user == 0 and comp == 1:
    print("You lose!\n")
  elif user == 0 and comp == 2:
    print("You win!\n")
  elif user == 1 and comp == 0:
    print("You win!\n")
  elif user == 1 and comp == 2:
    print("You lose!\n")
  elif user == 2 and comp == 0:
    print("You lose!\n")
  elif user == 2 and comp == 1:
    print("You win!\n")
