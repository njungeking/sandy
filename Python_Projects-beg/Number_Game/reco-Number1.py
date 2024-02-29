# A recap of the Number Game Project.

from random import randint

EASY = 10
HARD = 5

def diff():
  level = input("Which level do you wish to play? 'easy' or 'hard'? ").lower()
  if level == "easy":
    return EASY
  elif level == "hard":
    return HARD

def check(guess, answer, turns):
  if guess > answer:
    print("Too High!")
    return turns - 1
  elif guess < answer:
    print("Too Low!")
    return turns - 1
  else:
    print(f"Congratulations. You got the answer: {answer}!")

def the_game():
    
  print("Welcome to the Number Game!")
  print("I am thinking of a number between 1 and 100..")
  answer = randint(1,100)
  print(f"Psst! The answer is: {answer}!")
  turns = diff()
  guess = 0
  while guess != answer:
      
    print(f"You have: {turns}, chances remaining!")
    guess = int(input("Guess a number: "))
    turns = check(guess, answer, turns)
    if turns == 0:
      print(f"You have ran out of chances! The answer is {answer}!")
      return
    elif guess != answer:
      print("Guess again!")

the_game()
