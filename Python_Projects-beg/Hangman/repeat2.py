# Another reacp of repeatability in the Hangman's project.

import random
print("Welcome to a Hangman's game!\n")
animals = ["deer", "penguin", "ardvark", "cheetah"]
word = random.choice(animals)
size = len(word)
display = []
print(f"The animal is {word}\n")

for _ in range(size):
  display += '_'
print(display)

end = False

while not end:
  guess = input("Please enter any letter that you wish: \n").lower()
  
  for pos in range(size):
    letter = word[pos]
    if letter == guess:
      display[pos] = letter
  print(display)

  if not '_' in display:
    end = True
    print("You win!\n")
