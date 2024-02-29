# A recap of the Higher-Lower game Project.

# Import the logo and the vs.
# Import the data.
# Clear the screen for the next round.
# Import the clear function from replit.
from art import logo,vs
from game_data import data
import random
from replit import clear

# Present the data of the two sets in the desired format.
def format(account):
  """Returns the desired information in a linear format."""
  account_name = account["name"]
  account_job = account["description"]
  account_country = account["country"]
  return f"{account_name}, a {account_job}, from {account_country}"

# Create a function that compares the guess,
# followers_a and followers_b and returns,
# True or False.
def compare(guess, followers_a, followers_b):
  """A comparison function that compares different inputs."""
  if followers_a > followers_b:
    return guess == 'a'
  else:
    return guess == 'b'

print(logo)
score = 0

# Make Option B become A in the next round.
account_b = random.choice(data)

cont_game = True
while cont_game:
    
  # Generate the two random sets of data.
  account_a = account_b
  account_b = random.choice(data)
  while account_b == account_a:
    account_b = random.choice(data)
  
  print(f"Compare A: {format(account_a)}.")
  print(vs)
  print(f"Against B: {format(account_b)}.")
  
  followers_a = account_a["follower_count"]
  followers_b = account_b["follower_count"]
  guess = input("Who has the most followers? 'A' or 'B'? ").lower()
  clear()
  print(logo)
  
  is_correct = compare(guess, followers_a, followers_b)
  if is_correct:
    score += 1
    print(f"You are right! Your score is {score}.")
  else:
    cont_game = False
    print(f"Sorry. You are wrong. Your score is: {score}.")
