from replit import clear
from art import logo

def highest_bidder(total_bids):
  highest = 0
  winner = ""
  for bidder in total_bids:
    amount = total_bids[bidder]
    if amount > highest:
      highest = amount
      winner = bidder
  print(f"The highest bidder is {winner} with a bid of $ {amount}!\n")

print(logo)
print("Welcome to a silent auction program!\n")
bids = {}
cont = True
while cont:
  name = input("Please enter your name: \n")
  bid = int(input("Please enter the amount you wish to bid: \n"
                 "$ "))
  bids[name] = bid
  other = input("Are there other bidders? \n")
  if other == "yes":
    clear()
  elif other == "no":
    cont = False
    highest_bidder(bids)
