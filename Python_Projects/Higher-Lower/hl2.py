# A second attempt at the Higher-Lower Game project.

# Import the logo and the vs.
# Import the data set.
# import the random module.
# import the clear function.
from art import logo,vs
from game_data import data
import random
from replit import clear
print(logo)
score = 0

# Make the account_b become account_a in the next round.
account_b = random.choice(data)

# Format the data sets as shown in the final program.
# Create a function that can be used for both accounts to format the data.
def compare(account):
  account_name = account["name"]
  account_job = account["description"]
  account_country = account["country"]
  return f"{account_name}, a {account_job}, from {account_country}."

# A way to check whether the user is right.
# A function that takes the guess, and the accounts[followers] as,
# inputs and returns whether the guess is true or false.
def checker(guess,followers_a,followers_b):
  if followers_a > followers_b:
    return guess == 'a'
  else:
    return guess == 'b'

# Make the program repeatable.
cont_game = True
while cont_game:
    
  # Generate random lists of A and B.
  account_a = account_b
  account_b = random.choice(data)
  while account_b == account_a:
    account_b = random.choice(data)
  
  data_a = print(f"Compare A: {compare(account_a)}")
  print(vs)
  data_b = print(f"Against B: {compare(account_b)}")
  
  # Ask the user to make a guess between the two opptions.
  guess = input("Who has more followers between 'A' and 'B'? ").lower()
  
  followers_a = account_a["follower_count"]
  followers_b = account_b["follower_count"]
  
  is_correct = checker(guess, followers_a, followers_b)
  if is_correct:
    clear()
    print(logo)
    score += 1
    print(f"You are right! Your current score is: {score}")
  else:
    cont_game = False
    print(f"Sorry, You're wrong. Your final score is {score}")
