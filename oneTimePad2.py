import string
from ciphers import Cipher;


class OneTimePad(Cipher):
    def _tobits(self, s):
        result = []
        for c in s:
            bits = bin(ord(c))[2:]
            bits = '00000000'[len(bits):] + bits
            result.extend([int(b) for b in bits])
        return result

    def _frombits(self, bits):
        chars = []
        for b in range(len(bits) // 8):
            byte = bits[b * 8:(b + 1) * 8]
            chars.append(chr(int(''.join([str(bit) for bit in byte]), 2)))
        return ''.join(chars)

    def encrypt(self, text, key):
        answer_bits = [];
        text_bits = self._tobits(text)
        key_bits = self._tobits(key)
        for index in range(0, len(text_bits)):
            answer_bits.append(text_bits[index] | key_bits[index])
        return self._frombits(answer_bits)

    def decrypt(self, text, key):
        answer_bits = [];
        text_bits = self._tobits(text)
        key_bits = self._tobits(key)
        for index in range(0, len(text_bits)):
            answer_bits.append(text_bits[index] | key_bits[index])
        return self._frombits(answer_bits)


jon = OneTimePad()
bob = jon.encrypt("joniscool", "ccccccccc")
print(bob)
print(jon.decrypt(bob, "ccccccccc"))
