from replit import clear
from art import logo

def highest_bidder(total_bids):
  highest = 0
  winner = ""
  for bidder in total_bids:
    bid_amount = total_bids[bidder]
    if bid_amount > highest:
      highest = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of $ {highest}!\n")

print(logo)
print("Welcome to a silent auction program!\n")
bids = {}

cont = True
while cont:
  name = input("Please enter your name: \n")
  bid = int(input("Please enter your bid: \n"
                 "$ "))
  bids[name] = bid
  other = input("Are there other bidders? \n")
  if other == "yes":
    clear()
  elif other == "no":
    cont = False
    highest_bidder(bids)
