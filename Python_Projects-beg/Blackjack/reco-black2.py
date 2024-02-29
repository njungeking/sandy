# A second recap at the Blackjack Project.

import random
from art import logo
from replit import clear

def deck_pick():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  pick = random.choice(cards)
  return pick

def calc(cards):
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
    return "You Lose. Opponent has a Blackjack!"
  elif user_score == 0:
    return "You Win. You have a Blackjack!"
  elif user_score > 21:
    return "You Lose. You went Overboard!"
  elif comp_score > 21:
    return "You Win. Opponent went Overboard!"
  elif user_score > comp_score:
    return "You win!"
  else:
    return "You Lose!"

def the_game():
    
  print(logo)
  print("Welcome to a sample Blackjack game!")
  user_cards = []
  comp_cards = []
  
  for x in range(2):
    user_cards.append(deck_pick())
    comp_cards.append(deck_pick())
  
  end_game = False
  while not end_game:
      
    user_score = calc(user_cards)
    comp_score = calc(comp_cards)
    
    print(f"Your cards are: {user_cards} and your score is: {user_score}")
    print(f"The machine's first card is: {comp_cards[0]}")
    
    if comp_score == 0 or user_score == 0 or user_score > 21:
      end_game = True
    else:
      cont = input("Do you wish to draw another card? 'y' or 'n'? ")
      if cont == 'y':
        user_cards.append(deck_pick())
        user_score = calc(user_cards)
        if comp_score != 0 and comp_score < 17:
          comp_cards.append(deck_pick())
          comp_score = calc(comp_cards)
      else:
        end_game = True
  print(f"Your final cards are: {user_cards} and your final score is {user_score}")
  print(f"The machine's final cards are: {comp_cards} and the machine's final score is {comp_score}")
  print(compare(user_score,comp_score))

while input("Do you wish to play a Blackjack game? 'y' or 'n'? ") == 'y':
  clear()
  the_game()
