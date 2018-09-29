from affine import Affine
from atbash import Atbash
from caesar import Caesar
from kword import KWord
import random
import string
from oneTimePad import OneTimePad


def format_text(text_in):
    """this formats texts into 5 character blocks"""
    new_text = ''
    for index in range(0, len(text_in)):
        if index % 5 == 0:
            new_text += " "
        new_text += text_in[index]
    if len(text_in) % 5 != 0:
        how_many = 5 - (len(text_in) % 5)
        for _ in range(0, how_many):
            a_letter = random.choice(string.ascii_lowercase);
            new_text += a_letter
    return new_text


while True:
    operation = input("Please enter 'encrypt', 'decrypt', or 'q' to quit: ")
    # variable for processing text
    text = ''
    # answer if the person wants block formatting.
    block_answer = ''
    if operation.lower() == "encrypt":
        # strips spaces from input, all the ciphers I wrote account for spaces except the one-time-pad
        text = input("Please enter text to encrypt: ").replace(" ", "");
        # ec = encrypted
        ec_text = ''
        block_answer = input("Do you want to encrypted text in five character blocks?(y/n)")
        if block_answer == 'y':
            # format the text in to the right format but gets rid of spaces to do the padding correctly
            # the text is re-formated later
            text = format_text(text).replace(" ", "")
        one_time_answer = input("Are you using a one-time-pad? (y/n)")
        if one_time_answer.lower() == 'y':
            one_key = input("Please enter a key the same length as the text to be encrypted, \n " +
                            "The length of the text is {}:".format(len(text)))
            one_key_generator = OneTimePad()
            # makes an instance of one-time-pad and applies it
            text = one_key_generator.encrypt(text, one_key)
        print("Available ciphers... 'affine' 'atbash' 'caesar' 'keyword' ")
        cipherSelection = input("Please select a cipher: ")
        if cipherSelection.lower() == "affine":
            # gathers the other needed input to encrypt using affine cipher
            co_prime = input("Please pick a co-prime of 26: (i.e. 15, 17, 19...)")
            key = input("Please pick a key of the cipher encryption, a number 1-26: ")
            affine = Affine(int(co_prime), int(key))
            ec_text = affine.encrypt(text)
        elif cipherSelection.lower() == "atbash":
            # atbash doesn't need additional parameters
            atbash = Atbash();
            ec_text = atbash.encrypt(text)
        elif cipherSelection.lower() == "keyword":
            # gets keyword for the encrypting of the keyword cipher
            keyword_in = input("Please enter in a keyword: ")
            kword = KWord(keyword_in)
            ec_text = kword.encrypt(text)
        elif cipherSelection.lower() == "caesar":
            # gets the offset needed
            offset = input("Please enter in an offset: ")
            caesar = Caesar(int(offset))
            ec_text = caesar.encrypt(text).lower()
        else:
            break
        if block_answer == 'y':
            # re-apply formatting if block formatting is chosen.
            # this re-adds the spaces where above the extra letters were added.
            print("Your encrypted text is: {}".format(format_text(ec_text)))
        else:
            # prints ec-text without the block formatting
            print("Your encrypted text is: {}".format(ec_text))
    elif operation.lower() == "decrypt":
        original_text = input("Please enter text to decrypt: ").replace(" ", "");
        print("Available ciphers... 'affine' 'atbash' 'caesar' 'keyword' ")
        cipherSelection = input("Please select a cipher: ")
        if cipherSelection.lower() == "affine":
            co_prime = input("Please pick a co-prime of 26: (i.e. 15, 17, 19...)")
            key = input("Please pick a key of the cipher encryption, a number 1-26: ")
            affine = Affine(int(co_prime), int(key))
            text = affine.decrypt(text)
        elif cipherSelection.lower() == "atbash":
            atbash = Atbash();
            text = atbash.decrypt(text)
        elif cipherSelection.lower() == "keyword":
            keyword_in = input("Please enter in a keyword: ")
            kword = KWord(keyword_in)
            text = kword.decrypt(text)
        elif cipherSelection.lower() == "caesar":
            offset = input("Please enter in an offset: ")
            caesar = Caesar(int(offset))
            text = caesar.decrypt(text)
        else:
            break
        oneTimeAnswer = input("Are you using a one-time-pad? (y/n)")
        # one-time-pad done as the last thing, because it was done first in encryption
        if oneTimeAnswer.lower() == 'y':
            print("Please enter a key the same length as the text to be decrypted,")
            one_key = input("The length of the text is {}:".format(len(original_text)))
            one_key_generator = OneTimePad()
            text = one_key_generator.decrypt(text.lower(), one_key)
        print("Your decrypted text is: {}".format(text))
    else:
        # if anything other than encrypt or decrypt is chosen the while loop ends
        break
