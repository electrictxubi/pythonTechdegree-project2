import string
from ciphers import Cipher


class Atbash(Cipher):
    def __init__(self):
        # letter to number dict for conversion
        self.letter_numbers = dict(zip(string.ascii_lowercase, range(1, 27)))
        # number to letter dice for conversion
        self.numbers_letters = dict(zip(range(1, 27), string.ascii_lowercase))

    def encrypt(self, text):
        """Encrypts the text using the Atbash cipher"""
        output = []
        for letter in text:
            # this try is to account for spaces
            try:
                # convert letter to number
                number = self.letter_numbers[letter.lower()]
                # this formula convers a=z b=y ... z=a got it from wikipedia
                equivalent = (-(number) % 26) + 1
                # convert encrypted number back to letter and append to output list
                output.append(self.numbers_letters[equivalent])
            except KeyError:
                output.append(' ')

        return ''.join(output)

    def decrypt(self, text):
        """Decrypts the text using the Atbash cipher"""
        # exactly the same logic as above
        output = []
        for letter in text:
            try:
                number = self.letter_numbers[letter.lower()]
                equivalent = (-(number) % 26) + 1
                output.append(self.numbers_letters[equivalent])
            except KeyError:
                output.append(' ')
        return ''.join(output)

