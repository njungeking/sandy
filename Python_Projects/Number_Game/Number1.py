# Number Guessing Game Project.

from random import randint
EASY = 10
HARD = 5

def check_answer(guess,answer,turns):
  """Checks whether the user's guess is equal to the answer."""
  if guess > answer:
    print("Too High!")
    return turns - 1
  if guess < answer:
    print("Too Low!")
    return turns - 1
  else:
    print(f"Congratulations. You are Correct! The answer is {answer}")

def set_difficulty():
  """Sets the difficulty which the user needs and subsequently the turns available."""
  level = input("Which level do you wish to play? 'easy' or 'hard'? ")
  if level == "easy":
    return EASY
  else:
    return HARD

def the_game():
    
  print("Welcome to a sample Number Guessing game!")
  print("I am thinking of a number between 1 and 100.")
  answer = randint(1,100)
  #print(f"Psst! The correct answer is {answer}")
  
  turns = set_difficulty()
  
  guess = 0
  while guess != answer:
      
    print(f"You are remaining with: {turns} chances!")
    guess = int(input("Guess a number: "))
    turns = check_answer(guess, answer, turns)
    
    if turns == 0:
      print("You have ran out of chances. You Lose!")
      print(f"The answer is {answer}!")
      return
    elif guess != answer:
      print("Guess again!")

the_game()
