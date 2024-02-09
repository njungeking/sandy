alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']

print("Welcome to a Ceaser Cypher program!\n")
option = input("Do you wish to 'encrypt' or 'decrypt'? \n")
text = input("Please put in the words that you would like to \n"
            "work with: \n")
shift = int(input("Please enter the value by which you wish to move: \n"))

def encrypt(inp,move):
  word = ""
  for let in inp:
    pos = alphabet.index(let)
    new_pos = pos + move
    new_let = alphabet[new_pos]
    word += new_let
  print(f"The encrypted word is {word}\n")

def decrypt(enc,move):
  orig = ""
  for let in enc:
    pos = alphabet.index(let)
    orig_pos = pos - move
    orig_letter = alphabet[orig_pos]
    orig += orig_letter
  print(f"The decrypted word is {orig}\n")

if option == "encrypt":
  encrypt(inp=text,move=shift)
elif option == "decrypt":
  decrypt(enc=text,move=shift)
else:
  print("Wrong entry. Please restart the program!\n")
