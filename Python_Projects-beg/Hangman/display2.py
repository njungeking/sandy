# Display list on Hangan project.

import random
word_list = ["aardvark", "baboon", "camel"]
word=random.choice(word_list)
print("Welcome to a Hangman game!\n")
print(f"The word is {word}\n")
display=[]
size=len(word)

for let in range(size):
  display += '_'
print(display)

guess=input("\nPlease enter any letter: \n")

for i in range(size):
  letter=word[i]
  if letter == guess:
    display[i] = letter

print(display)
