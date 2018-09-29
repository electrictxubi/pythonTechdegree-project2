import string
from ciphers import Cipher


class OneTimePad(Cipher):
    def __init__(self):
        # alphabet variables used to convert
        self.alphabet = string.ascii_lowercase
        self.alphabet_list = list(self.alphabet)

    def encrypt(self, text, key):
        """applies padding using key of same length as the cleartext"""
        output = ''
        for index, char in enumerate(text):
            # index where current character from text is
            char_index = self.alphabet.index(char)
            # index where the current key character from key is
            key_index = self.alphabet_list.index(key[index])

            # mathemagic stolen from wikipedia to apply padding
            cipher = (key_index + char_index) % 26
            # add character to output string
            output += self.alphabet[cipher]

        return output

    def decrypt(self, text, key):
        """decrypts the padding using a key of the same length as the encrypted text"""
        output = '';
        for index, char in enumerate(text):
            # same as encrypt
            char_index = self.alphabet.index(char)
            key_index = self.alphabet_list.index(key[index])
            # different wikipedia stolen mathemagic to decrypt padding
            cipher = (char_index - key_index) % 26
            output += self.alphabet[cipher]
        return output;

