alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(text, shift):
  cipher_text = ""
  for i in range(0,len(text)):
    index = alphabet.index(text[i])
    cipher_text += alphabet[index + shift]
  print(cipher_text)

def decrypt(text, shift):
  plaintext = ""
  for i in range(0,len(text)):
    index = alphabet.index(text[i])
    plaintext += alphabet[index - shift]
  print(plaintext)

validResponse = False

while not validResponse:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt, type 'end' to end the program:\n")
  if direction == "end":
    validResponse = True
    break
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  if direction == "encode":
    validResponse = True
    encrypt(text, shift)
  elif direction == "decode":
    validResponse = True
    decrypt(text, shift)
  else:
    print("Invalid response.")