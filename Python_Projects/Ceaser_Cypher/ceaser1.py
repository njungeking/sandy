# Ceaser-Cypher project.

alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd',
    'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
    't', 'u', 'v', 'w', 'x', 'y', 'z'
]

def encrypt(inp, code):
    word = ""
    for letter in inp:
        pos = alphabet.index(letter)
        pos += code
        new_letter = alphabet[pos]
        word += new_letter
    print(word)


def decrypt(out, code):
    output = ""
    for letter in out:
        pos = alphabet.index(letter)
        pos -= code
        orig_let = alphabet[pos]
        output += orig_let
    print(output)


print("Welcome to a Ceaser-Cypher program!\n")
direction = input("Do you want to encrypt or decrypt your message?\n")

if direction == "encrypt":
    user_enc = input("Please enter the word you word to encrypt: \n")
    shift = int(input("By what value do you wish to shift? \n"))
    encrypt(inp=user_enc, code=shift)
elif direction == "decrypt":
    user_dec = input("Please enter the word that you want to decrypt: \n")
    shift = int(input("By what value do you wish to shift? \n"))
    decrypt(out=user_dec, code=shift)
