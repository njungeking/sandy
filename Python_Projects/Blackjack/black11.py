############### Blackjack Project #####################
import random
is_game_over = False

def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  rand = random.choice(cards)
  return rand

def calculate_score(cards):

  if sum(cards) == 21 and len(cards) == 2:
    return 0

  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)

  return sum(cards)

user_cards = []
computer_cards = []
for _ in range(2):
  user_cards.append(deal_card())
  computer_cards.append(deal_card())

while not is_game_over:
    
  user_score = calculate_score(user_cards)
  computer_score = calculate_score(computer_cards)
  
  if user_score == 0 or computer_score == 0 or user_score > 21:
    is_game_over = True

  cont = input("Would you like to draw another card? 'y' or 'n'? ")
  if cont == 'y':
    user_cards.append(deal_card())
  else:
    is_game_over = True

while computer_score != 0 and computer_score < 17:
  computer_cards.append(deal_card())
  computer_score = calculate_score(computer_cards)

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
