# Attempt #3 on the Blackjack project.

from replit import clear
import random
from art import logo

def card_pick():
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
    return "It is a Draw!"
  elif comp_score == 0:
    return "You Lose! Opponent has a Blackjack!"
  elif user_score == 0:
    return "You Win! You have a Blackjack!"
  elif user_score > 21:
    return "You went over! You Lose!"
  elif comp_score > 21:
    return "Oppenent went over! You Win!"
  elif user_score > comp_score:
    return "You Win!"
  else:
    return "You Lose!"

def play():
    
  print(logo)
  print("Welcome to a sample Blackjack game!\n")
  user_cards = []
  comp_cards = []
  game_over = False
  
  for _ in range(2):
    user_cards.append(card_pick())
    user_cards.append(card_pick())
  
  while not game_over:
      
    user_score = calc(user_cards)
    comp_score = calc(comp_cards)
    print(f"Your cards are: {user_cards},Your score is: {user_score}")
    print(f"Comp's first card is: {comp_cards[0]}")
    
    if user_score == 0 or comp_score == 0 or user_score > 21:
      game_over = True
    else:
      cont = input("Do you wish to continue with the game? 'y' or 'n'? ")
      if cont == 'y':
        user_cards.append(card_pick())
      else:
        game_over = True
  
  while comp_score != 0 and comp_score < 17:
    comp_cards.append(card_pick())
    comp_score = calc(comp_cards)

  print(f"Your final hand is {user_cards} and final score is {user_score}")
  print(f"Computer's final hand is {comp_cards} and final score is {comp_score}")
  print(compare(user_score,comp_score))

the_game = input("Do you want to play a game of Blackjack? 'y' or 'n'? ")
while the_game == 'y':
  clear()
  play()
