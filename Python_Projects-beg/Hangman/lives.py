# Lives reduction in the Hangman project.

import random

animals = ["ardvark", "deer", "pig", "cheetah"]
word = random.choice(animals)
size = len(word)
print(f"The word is {word}")
display = []
lives = 6

for _ in range(size):
    display += '_'
print(f"{' '.join(display)}")

end = False

while not end:
    guess = input("Please enter any letter you wish: \n")

    for pos in range(size):
        letter = word[pos]
        if letter == guess:
            display[pos] = letter
    print(f"{' '.join(display)}")

    if guess not in word:
        lives -= 1
        if lives == 0:
            print("You lose. Game over!\n")
            end = True
      
    if '_' not in display:
        end = True
        print("You win!\n")

