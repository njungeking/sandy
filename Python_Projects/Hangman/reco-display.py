# A recap of the display on the Hangman project.

import random
animals = ["aardvark","donkey","camel","hippo"]
word=random.choice(animals)
print("Welcome to a Hangman's game!\n")
print(f"The word is {word}\n")
size=len(word)
display=[]

for _ in range(size):
  display += '_'
print(display)

guess=input("\nPlease enter any letter: ")

for pos in range(size):
  letter = word[pos]
  if letter == guess:
    display[pos] = letter

print(display)
