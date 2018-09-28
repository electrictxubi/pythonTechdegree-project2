from affine import Affine
from atbash import Atbash
from caesar import Caesar
from kword import KWord
from oneTimePad import OneTimePad

# Pleae enter in the plaintext:
#
# Ask if one time pad
# ask for key if yes
# Please enter in the cipher you want to use:
# Print available if ciphers..:
#
# Settle special cipher cases
while(True):
    oneTimeFlag = False
    operation = input("Please enter 'encrypt', 'decrypt', or 'q' to quit: ")
    text = ''
    oneText = text
    if operation == "encrypt":
        text = input("Please enter text to encrypt: ")
        oneTimeAnswer = input("Are you using a one-time-pad? (y/n)")
        if oneTimeAnswer.lower() == 'y':
            oneKey = input("Please enter a key the same length as the text to be encrypted, \n " +
                           "The length of the text is {}:".format(len(text)))
            oneKeyGenerator = OneTimePad()
            oneText = oneKeyGenerator.encrypt(text, oneKey)
            oneTimeFlag = True
        print("Available ciphers... 'affiene' 'atbash' 'caesar' 'keyword' ")
        cipherSelection = input("Please select a cipher: ")
        if cipherSelection.lower() == "affeine":
            coprime = input("Please pick a co-prime of 26: (i.e. 15, 17, 19...)")
            key = input("Please pick a key of the cipher encryption, a number 1-26: ")
            affine = Affine(coprime, key);
            print("Your encrypted text is: ")
            print(affine.encrypt(oneText))

    elif operation == "decrypt":
        pass
    else:
        break
