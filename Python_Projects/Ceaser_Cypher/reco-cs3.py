# A recap of step #3 of the Ceaser-Cypher Project.

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']

print("Welcome to a Ceaser-Cypher program!\n")
direction = input("Please enter whether you want to 'encode' or 'decode' your message: \n").lower()
text = input("Please enter the message that you wish to work with: \n").lower()
shift = int(input("Please enter the shift number that you wish: \n"))

def ceaser(way,mes,move):
  word = ""
  if way == "decode":
    move *= -1
  for let in mes:
    pos = alphabet.index(let)
    new_pos = pos + move
    new_let = alphabet[new_pos]
    word += new_let
  print(f"The {way}d message is {word}\n")

ceaser(way=direction,move=shift,mes=text)
