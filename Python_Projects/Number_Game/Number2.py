# A second attempt at the Number Game Project.

from random import randint
EASY = 10
HARD = 5

def set_dif():
  dif = input("Which difficulty would you prefer? 'hard' or 'easy'? ")
  if dif == 'easy':
    return EASY
  elif dif == 'hard':
    return HARD

def checker(guess,answer,turns):
  if guess > answer:
    print("Too High!")
    return turns - 1
  elif guess < answer:
    print("Too Low!")
    return turns - 1
  else:
    print(f"Congratulations. The number is {answer}!")

def play():
    
  print("Welcome to a sample Number Game!")
  print("I am thinking of a number between 1 and 100..")
  answer = randint(1,100)
  print(f"Psst! The number is: {answer}!")
  turns = set_dif()

  guess = 0
  while guess != answer:
      
    print(f"You have {turns} chances remaining!")
    guess = int(input("Guess a number: "))
    turns = checker(guess,answer,turns)
    if turns == 0:
      print(f"You have ran out of chances. The answer is: {answer}!")
      return
    elif guess != answer:
      print("Guess again!")
play()
