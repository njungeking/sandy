# Attempt #4 on the Blackjack Project.

import random
from art import logo
from replit import clear

def deck_pick():
  """Picks a random card from the deck."""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  return random.choice(cards)

def calc(cards):
  """Calculates the sum of the cards of the user and the machine."""
  if sum(cards) == 21 and len(cards) == 2:
    return 0

  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  
  return sum(cards)

def compare(user_score,comp_score):
  if user_score == comp_score:
    return "Draw!"
  elif comp_score == 0:
    return "Opponent won with a Blackjack!"
  elif user_score == 0:
    return "You won with a Blackjack!"
  elif user_score > 21:
    return "You went over! You Lose!"
  elif comp_score > 21:
    return "Opponent went over! You Win!"
  elif user_score > comp_score:
    return "You Win!"
  else:
    return "You lose!"

def play():
    
  print(logo)
  print("Welcome to a sample Blackjack Game!\n")
  
  user_cards = []
  comp_cards = []
  
  for x in range(2):
    user_cards.append(deck_pick())
    comp_cards.append(deck_pick())
  
  game_over = False
  while not game_over:
      
    user_score = calc(user_cards)
    comp_score = calc(comp_cards)
    
    print(f"Your cards: {user_cards}, Your score: {user_score}")
    print(f"Machine's first card: {comp_cards[0]}")
  
    if comp_score == 0 or user_score == 0 or user_score > 21:
      game_over = True
    else:
      again = input("Would you like to deal again? 'y' or 'n'? ")
      if again == 'y':
        user_cards.append(deck_pick())
        user_score = calc(user_cards)
        if comp_score != 0 and comp_score < 17:
          comp_cards.append(deck_pick())
          comp_score = calc(comp_cards)
      else:
        print("Goodbye!")
        game_over = True
    
  print(f"Your final cards are: {user_cards} and your final score is {user_score}")
  print(f"Machine's final cards are: {comp_cards} and final Machine score is {comp_score}")
  print(compare(user_score,comp_score))
 
while input("Would you like to play a Blackjack game? 'y' or 'n'? ") == 'y':
  clear()
  play()
