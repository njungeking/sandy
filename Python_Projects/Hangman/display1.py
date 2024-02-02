# Hangman project build-up.

import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
print(f'Pssst, the solution is {chosen_word}.')
size=len(chosen_word)
display=[]

for letter in range(size):
  display += "_"
print(display)

guess = input("Guess a letter: ").lower()

for i in range(size):
  letter=chosen_word[i]
  if letter == guess:
    display[i] = letter

print(display)

