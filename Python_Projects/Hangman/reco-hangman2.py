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

# A second recap attempt of the Hangman's Project
# including the use of the ASCII Art.

print("Welcome to THE HANGMAN'S game!\n")
utensils = ["spoon", "knife", "fork", "plate", "cup"]
word = random.choice(utensils)
size = len(word)
#print(f"psst, the word is {word}")
display = []
lives = 6

for _ in range(size):
  display += '_'
print(f"{' '.join(display)}")

end = False
while not end:
  guess = input("Please enter any letter that you wish: \n")
  
  for pos in range(size):
    letter = word[pos]
    if letter == guess:
      display[pos] = letter
  print(f"{' '.join(display)}")

  if guess not in word:
    lives -= 1
    if lives == 0:
      print("You've Lost!\n")
      print(f"The word is {word}!")
      end = True

  print(stages[lives])
  
  if '_' not in display:
    print("You've Won!\n")
    end = True
