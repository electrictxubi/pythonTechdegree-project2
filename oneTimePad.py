import string
from ciphers import Cipher


class OneTimePad(Cipher):
    def __init__(self):
        self.alphabet = string.ascii_lowercase
        self.alphabet_list = list(self.alphabet)

    def encrypt(self, text, key):
        output = ''
        for index, char in enumerate(msg):
            char_index = self.alphabet.index(char)
            key_index = self.alphabet_list.index(key[index])

            cipher = (key_index + char_index) % 26
            output += self.alphabet[cipher]

        return output

    def decrypt(self, text):
        output = []
        for i, j in range(0, len(text)):
            try:
                text_numb = self.letter_numbers[text[i]];
                key_numb = self.letter_numbers[self.key[i]];
                decoded_char = self.numbers_letters[text_numb - key_numb]
                output.append(decoded_char)
            except KeyError:
                output.append(' ')
        return ''.join(output)


jon = OneTimePad("pinga")
encoded = jon.encrypt("this is cool")
print(encoded)
print(jon.decrypt(encoded))
