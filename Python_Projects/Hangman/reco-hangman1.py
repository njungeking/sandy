#Step 4

import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

# A recap of the Hangman's project including
# the ASCII Art.

print("Welcome to a Hangman's game!\n")
animals = ["deer", "antelope", "tiger", "rhino"]
word = random.choice(animals)
size = len(word)
print(f"psst, the word is {word}")
display = []
lives = 6

for _ in range(size):
  display += '_'
print(f"{' '.join(display)}")

endgame = False
while not endgame:
  guess = input("Please enter any letter you wish: \n")
  
  for pos in range(size):
    letter = word[pos]
    if letter == guess:
      display[pos] = letter
  print(f"{' '.join(display)}")

  if guess not in word:
    lives -= 1
    if lives == 0:
      print("You lose")
      endgame = True

  print(stages[lives])

  if '_' not in display:
    print("You Won!\n")
    endgame = True
