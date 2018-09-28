import string
from ciphers import Cipher


class OneTimePad(Cipher):
    def __init__(self):
        self.alphabet = string.ascii_lowercase
        self.alphabet_list = list(self.alphabet)

    def encrypt(self, text, key):
        output = ''
        for index, char in enumerate(text):
            char_index = self.alphabet.index(char)
            key_index = self.alphabet_list.index(key[index])

            cipher = (key_index + char_index) % 26
            output += self.alphabet[cipher]

        return output

    def decrypt(self, text, key):
        output = '';
        for index, char in enumerate(text):
            char_index = self.alphabet.index(char)
            key_index = self.alphabet_list.index(key[index])

            cipher = (char_index - key_index) % 26
            output += self.alphabet[cipher]
        return output;


jon = OneTimePad()
encoded = jon.encrypt("thisiscool", "absrdfjyyk")
print(encoded)
print(jon.decrypt(encoded, "absrdfjyyk"))

