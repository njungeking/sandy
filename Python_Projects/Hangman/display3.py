# Another attempt on display on Hangman project.

import random
word_list = ["aardvark", "baboon", "camel"]
choice=random.choice(word_list)
print("Welcome to a Hangman game!\n")
print(f"The word is: {choice}.\n")
length=len(choice)
display=[]

for letters in range(length):
  display += '_'
print(display)

guess=input("\nPlease enter a letter: \n\n")

for i in range(length):
  letter = choice[i]
  if letter == guess:
    display[i] = letter

print(display)
