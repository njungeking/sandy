# Attempt # 2 on the Blackjack Project.

import random
from art import logo
print(logo)
print("Welcome to a sample Blackjack game!\n")
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
game_over = False

def card_pick():
  """Deals new cards"""
  return random.choice(cards)

user_cards = []
comp_cards = []

for _ in range(2):
  user_cards.append(card_pick())
  comp_cards.append(card_pick())

def calculate(cards):
  """Calculates the total score of the cards"""
  if sum(cards) == 21 and len(cards) == 2:
    return 0

  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)

  return sum(cards)

while not game_over:
    
  user_score = calculate(user_cards)
  comp_score = calculate(comp_cards)

  print(f"Your cards are: {user_cards} and your score is: {user_score}")
  print(f"The Computer's cards are: {comp_cards} and its score is {comp_score}")
  
  if user_score == 0 or comp_score == 0 or user_score > 21:
    game_over = True
  else:
    cont = input("Do you wish to draw another card? 'y' or 'n'? ")
    if cont == 'y':
      user_cards.append(card_pick())
    else:
      game_over = True

  while comp_score != 0 and comp_score < 17:
    comp_cards.append(card_pick())
    comp_score = calculate(comp_cards)
