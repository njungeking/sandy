# A second attempt at the unification of functions in the Ceaser-Cypher project.

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def ceaser(prints,move,opt):
  word=""
  if opt == "decode":
    move *= -1
  for let in prints:
    pos = alphabet.index(let)
    new_pos = pos + move
    new_let = alphabet[new_pos]
    word += new_let
  print(f"The {opt}d message is {word}\n")

ceaser(prints=text,move=shift,opt=direction)
