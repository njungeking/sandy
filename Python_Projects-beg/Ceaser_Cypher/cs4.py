# A recap of step #4 of the Ceaser-Cypher Project.

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def ceaser(way,mes,move):
  word = ""
  if way == "decode":
    move *= -1
  for char in mes:
    if char in alphabet:
      pos = alphabet.index(char)
      new_pos = pos + move
      new_char = alphabet[new_pos]
      word += new_char
    else:
      word += char
  print(f"The {way}d message is {word}\n")

print("Welcome to a Ceaser-Cypher program!\n")

repeat = True
while repeat:
  
  direction = input("Please enter whether you want to 'encode' or 'decode' your message: \n").lower()
  text = input("Please enter the message that you wish to work with: \n").lower()
  shift = int(input("Please enter the shift number that you wish: \n"))
  shift = shift % 26
  
  ceaser(way=direction,move=shift,mes=text)
  
  go = input("Would you like to go again? \n")
  if go == "no":
    repeat = False
    print("Goodbye!\n")
