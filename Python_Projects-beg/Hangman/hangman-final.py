# Enhanced User XP in the Hangman's project.

import random
from replit import clear
from hangman_words import word_list
from hangman_art import stages,logo

print(logo)
print("\nWelcome to a Hangman's game!\n")
word = random.choice(word_list)
size = len(word)
#print(f"psst, the word is {word}")
display = []
lives = 6

for _ in range(size):
  display += '_'
print(f"{' '.join(display)}")

endgame = False
while not endgame:
  guess = input("Please guess any letter: \n")
  clear()

  if guess in display:
    print(f"You have already tried {guess}. Please \n"
    "enter another letter.")
  
  for pos in range(size):
    letter = word[pos]
    if letter == guess:
      display[pos] = letter
  print(f"{' '.join(display)}")

  if guess not in word:
    lives -= 1
    print(f"The letter {guess} is not in the word. \n"
    "You have lost a life!\n")
    if lives == 0:
      print("You have ran out of lives. GAME OVER!\n")
      print(f"The word is {word}!\n")
      endgame = True

  print(stages[lives])

  if '_' not in display:
    print("You've Won!\n")
    endgame = True
