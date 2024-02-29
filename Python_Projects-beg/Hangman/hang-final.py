# A recap of the final Hangman Project.

import random
from replit import clear
from hangman_words import word_list
from hangman_art import logo,stages

print(logo)
print("Welcome to a Hangman's game!\n")
word = random.choice(word_list)
size = len(word)
print(f"psst! The word is {word}!\n")
display = []
lives = 6

for _ in range(size):
  display += '_'
print(f"{' '.join(display)}")

endgame = False
while not endgame:
  
  guess = input("\nPlease guess any letter you wish: \n")
    
  clear()

  if guess in display:
    print(f"You have already entered {guess}! Try again!\n")
  
  for no in range(size):
    letter = word[no]
    if letter == guess:
      display[no] = letter
  print(f"{' '.join(display)}")

  if guess not in word:
    lives -= 1p
    print(f"The letter {guess} is not in the word. You've lost a life!\n")
    if lives == 0:
      print("You have ran out of lives! GAME OVER!\n")
      print(f"The word is {word}!\n")
      endgame = True

  print(stages[lives])

  if '_' not in display:
    print("You have Won!\n")
    endgame = True
