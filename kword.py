import string

from ciphers import Cipher


class KWord(Cipher):
    def __init__(self, kword=""):
        self.kword = kword.lower()[::-1]
        alphabet = list(string.ascii_lowercase)
        for letter in self.kword:
            alphabet.remove(letter);
            alphabet.insert(0, letter);
        self.letters = dict(zip(alphabet, string.ascii_lowercase))
        self.r_letters = dict(zip(string.ascii_lowercase, alphabet))

    def encrypt(self, text):
        """Encrypts the text using the Keyword cipher"""
        output = []
        for letter in text:
            # this try is to account for spaces
            try:
                # convert letter to encrypted letter
                encrypted_letter = self.letters[letter.lower()]
                # convert encrypted number back to letter and append to output list
                output.append(encrypted_letter)
            except KeyError:
                output.append(' ')

        return ''.join(output)

    def decrypt(self, text):
        """Decrypts the text using the Keyword cipher"""
        # exactly the same logic as above except r_letters or reversed letter list is used for decryption
        output = []
        for letter in text:
            try:
                regular_letter = self.r_letters[letter.lower()]
                output.append(regular_letter)
            except KeyError:
                output.append(' ')
        return ''.join(output)



