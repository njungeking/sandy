# A second recap of the Number Game Project.

from random import randint
EASY = 10
HARD = 5
def level():
  dif = input("Which difficulty level do you prefer? 'easy' or 'hard'? ").lower()
  if dif == "easy":
    return EASY
  elif dif == "hard":
    return HARD

def checker(guess, answer, turns):
  if guess > answer:
    print("Too High!")
    return turns - 1
  elif guess < answer:
    print("Too Low!")
    return turns - 1
  else:
    print(f"Congratulations! You got the answer is: {answer}!")

def play_game():
    
  print("Welcome to a Number Game!")
  print("I am thinking of a number between 1 and 100..")
  answer = randint(1,100)
  turns = level()
  guess = 0
  while guess != answer:
      
    print(f"You are remaining with: {turns} chances!")
    guess = int(input("Please guess a number between 1 and 100: "))
    turns = checker(guess, answer, turns)
    if turns == 0:
      print(f"You have ran out of chances. The answer is: {answer}!")
      return
    elif guess != answer:
      print("Guess again!")

play_game()
