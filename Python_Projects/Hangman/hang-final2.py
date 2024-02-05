# Another recap of the Hangman final project.

import random
from replit import clear
from hangman_words import word_list
from hangman_art import logo,stages

print(logo)
print("Welcome to a Hangman's Game!\n")
word = random.choice(word_list)
print(f"psst! The word is {word}!")
size = len(word)
display = []
lives = 6

for _ in range(size):
  display += '_'
print(f"{' '.join(display)}")

end = False
while not end:
    
  guess = input("Please guess any letter: \n")

  clear()

  if guess in display:
    print(f"You have already entered {guess}! Please try again!\n")
  
  for pos in range(size):
    letter = word[pos]
    if letter == guess:
      display[pos] = letter
  print(f"{' '.join(display)}")

  if guess not in word:
    lives -= 1
    print(f"{guess} is not in the word! You've lost a life!\n")
    if lives == 0:
      print("You have ran out of lives! GAME OVER!\n")
      print(f"The word is {word}!\n")
      end = True

  print(stages[lives])

  if '_' not in display:
    print("You have Won!\n")
    end = True
