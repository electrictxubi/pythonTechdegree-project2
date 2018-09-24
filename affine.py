import string
from ciphers import Cipher


class Affine(Cipher):
    def __init__(self, co_prime, key_number):
        # letter to number dict for conversion
        self.letter_numbers = dict(zip(string.ascii_lowercase, range(1, 27)))
        # number to letter dice for conversion
        self.numbers_letters = dict(zip(range(1, 27), string.ascii_lowercase))
        # this variable has to be a co-prime of 26 for the cipher to work
        self.co_prime = co_prime
        # this key number has to be between 1-26
        self.key_number = key_number

    def _getInverse(self, co_prime):
        """this calculates the multiplicative inverse needed in the decryption method"""
        result = 1

        for i in range(1, 26):

            if (co_prime * i) % 26 == 1:
                result = i

        return result

    def encrypt(self, text):
        """this encrpts the plaintext usung the affine cipher"""
        output = []
        for letter in text:
            # this try is to account for spaces
            try:
                # convert letter to number
                number = self.letter_numbers[letter.lower()]
                # this formula if got from wikipedia to encrypt
                equivalent = (self.co_prime * number + self.key_number) % 26
                # convert encrypted number back to letter and append to output list
                output.append(self.numbers_letters[equivalent])
            except KeyError:
                output.append(' ')

        return ''.join(output)

    def decrypt(self, text):
        """this decrypts the encoded messeage using the affine cipher"""
        output = []
        for letter in text:
            # this try is to account for spaces
            try:
                # convert letter to number
                number = self.letter_numbers[letter.lower()]
                # this formula if got from wikipedia to decrypt
                equivalent = self._getInverse(self.co_prime) * (number - self.key_number) % 26
                # convert encrypted number back to letter and append to output list
                output.append(self.numbers_letters[equivalent])
            except KeyError:
                output.append(' ')

        return ''.join(output)
