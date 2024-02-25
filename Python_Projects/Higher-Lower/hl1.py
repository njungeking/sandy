# Attempt #1 at the Higher Lower Game Project.

from game_data import data
from art import logo,vs
import random
from replit import clear

def format_data(account):
  """Takes the account data and returns the printable format."""
  account_name = account["name"]
  account_descr = account["description"]
  account_country = account["country"]
  return f"{account_name}, a {account_descr}, from {account_country}"

##Use an if statement to check if the user is correct.
def check_answer(guess, a_followers, b_followers):
  """Takes the user's guess and follower counts and returns if they got it right."""
  if a_followers > b_followers:
    return guess == 'a'
  else:
    return guess == 'b'

# Displey art.
print(logo)
score = 0
cont_game = True
account_b = random.choice(data)

# Make the game repeatable.
while cont_game:

  # Generate a random account from game_data.

  # Make the account at position B become the next account at position A.
  account_a = account_b
  account_b = random.choice(data)
  while account_a == account_b:
    account_b = random.choice(data)
  
  print(f"Compare A: {format_data(account_a)}")
  print(vs)
  print(f"Against B: {format_data(account_b)}")
  
  # Ask the user for a guess.
  guess = input("Who has more followers, 'A' or 'B''? ").lower()
  
  # Check if the user is correct.
  ## Get the followers of each account.
  a_followers = account_a["follower_count"]
  b_followers = account_b["follower_count"]
  is_correct = check_answer(guess, a_followers, b_followers)

  # Clear the screen between rounds.
  clear()
  print(logo)
  
  # Give the user feedback on their guess.
  # Score keeping.
  if is_correct:
    score += 1
    print(f"You are right! Your current score is: {score}")
  else:
    cont_game = False
    print(f"Sorry, That's wrong. Final score: {score}")
