import random
import string
print(2**3)
chars=" "+string.punctuation + string.digits + string.ascii_letters
chars=list(chars)
key=chars.copy()

random.shuffle(key)
# print(chars)
# print(key)

plain_text=input("Enter a message to encrypt: ")
cipher_text=''

for letter in plain_text:
    index=chars.index(letter)
    cipher_text+=key[index]

print(f"Encrypted message: {cipher_text}")

decipher2=input("Enter msg to decipher: ")
decipher=""

for i in decipher2:
    index=key.index(i)
    decipher+=chars[index]

print(f"Decrypted message: {decipher}")