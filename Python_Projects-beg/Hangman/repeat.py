# Introducing repeatability in the Hangman project.

import random
animals = ["ardvark","hyena","rhino","pig","donkey"]
print("Welcome to the Hangman game!\n")
word=random.choice(animals)
size=len(word)
display=[]
print(f"The word is {word}")

for _ in range(size):
  display += '_'
print(display)

end = False

while not end:
  guess=input("Please enter any letter that you wish: \n").lower()
  
  for pos in range(size):
    letter = word[pos]
    if letter == guess:
      display[pos] = letter
  print(display)

  if not '_' in display:
    end = True
    print("You win!\n")
