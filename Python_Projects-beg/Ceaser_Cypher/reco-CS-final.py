# A recap of the final Caeser-Cipher Project.

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caeser(move,inp,opt):
  word = ""
  if opt == "decode":
    move *= -1
  for let in inp:
    if let in alphabet:
      pos = alphabet.index(let)
      new_pos = pos + move
      new_let = alphabet[new_pos]
      word += new_let
    else:
      word += let
  print(f"The {opt}d word is {word}\n")

from art import logo
print(logo)

cont = True
while cont:
  print("Welcome to a Caeser-Cypher program!\n")
  dir = input("Please choose whether you wish to 'decode' or 'encode': \n").lower()
  text = input("Please enter the words that you wish to work with: \n").lower()
  shift = int(input("Please enter the value you wish to move with: \n"))
  shift = shift % 26
  
  caeser(move=shift,opt=dir,inp=text)
  att = input("Would you like to run the program again? \n")
  if att == "no":
    cont = False
    print("Goodbye!")
