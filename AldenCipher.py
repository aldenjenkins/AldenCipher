"""
:author: Alden Jenkins
:date: 10/2/17
:purpose: test the transfer of encrypted data over socket communication using object oriented programming
"""

# lower_case_alphabet = OrderedDict([
#     ('a', 1),
#     ('b', 2),
#     ('c', 3),
#     ('d', 4),
#     ('e', 5),
#     ('f', 6),
#     ('g', 7),
#     ('h', 8),
#     ('i', 9),
#     ('j', 10),
#     ('k', 11),
#     ('l', 12),
#     ('m', 13),
#     ('n', 14),
#     ('o', 15),
#     ('p', 16),
#     ('q', 17),
#     ('r', 18),
#     ('s', 19),
#     ('t', 20),
#     ('u', 21),
#     ('v', 22),
#     ('w', 23),
#     ('x', 24),
#     ('y', 25),
#     ('z', 26),
#     (' ', 27)
# ])
# lower_case_alphabet = {'a': 1,
#     'b': 2,
#     'c': 3,
#     'd': 4,
#     'e': 5,
#     'f': 6,
#     'g': 7,
#     'h': 8,
#     'i': 9,
#     'j': 10,
#     'k': 11,
#     'l': 12,
#     'm': 13,
#     'n': 14,
#     'o': 15,
#     'p': 16,
#     'q': 17,
#     'r': 18,
#     's': 19,
#     't': 20,
#     'u': 21,
#     'v': 22,
#     'w': 23,
#     'x': 24,
#     'y': 25,
#     'z': 26,
#     ' ': 27,
# }

lower_case_alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
upper_case_alphabet=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

# upper_case_alphabet = OrderedDict([
#     ('A', 1),
#     ('B', 2),
#     ('C', 3),
#     ('D', 4),
#     ('E', 5),
#     ('F', 6),
#     ('G', 7),
#     ('H', 8),
#     ('I', 9),
#     ('J', 10),
#     ('K', 11),
#     ('L', 12),
#     ('M', 13),
#     ('N', 14),
#     ('O', 15),
#     ('P', 16),
#     ('Q', 17),
#     ('R', 18),
#     ('S', 19),
#     ('T', 20),
#     ('U', 21),
#     ('V', 22),
#     ('W', 23),
#     ('X', 24),
#     ('Y', 25),
#     ('Z', 26),
#     (' ', 27)
# ])

# upper_case_alphabet = {
#     'A': 1,
#     'B': 2,
#     'C': 3,
#     'D': 4,
#     'E': 5,
#     'F': 6,
#     'G': 7,
#     'H': 8,
#     'I': 9,
#     'J': 10,
#     'K': 11,
#     'L': 12,
#     'M': 13,
#     'N': 14,
#     'O': 15,
#     'P': 16,
#     'Q': 17,
#     'R': 18,
#     'S': 19,
#     'T': 20,
#     'U': 21,
#     'V': 22,
#     'W': 23,
#     'X': 24,
#     'Y': 25,
#     'Z': 26,
#     ' ': 27,
# }

class AldensEncryptions(object):

    def __init__(self, the_message, the_key):
        """
        No Default constructor for this Object.

        :param message: <str> the message to be sent.
        :param key: <str> the key to encrypt the message with.
        """
        self.message = the_message
        self.key = the_key

    def get_message(self):
        return self.message

    def get_key(self):
        return self.key

    def set_message(self, the_message):
        self.message = the_message

    def set_key(self, the_key):
        self.key = the_key


    """
    """"""""""""""""""CAESAR""""""""""""""""""""
    """

    def encrypt_caesar(self):
        """
        Use a simple Caesar Cipher to encrypt the message.

        :return: the encrypted version of the self.message plaintext
        """

        # get the sum of character values in the key
        rot = sum([lower_case_alphabet.index(charKey)+1 for charKey in self.key])%len(lower_case_alphabet)

        # fill the cipher_text list for the same length of the message
        cipher_text = [""] * len(self.message)

        # split the message into individual characters
        chars = [char for char in self.message]

        # sequentially add characters to the cipher_text list
        for i in range(len(chars)):
            if chars[i] is " ":
                cipher_text[i] = " "
            elif chars[i].lower() != chars[i]:
                cipher_key_index = (upper_case_alphabet.index(chars[i])+1 + rot) % len(upper_case_alphabet)
                cipher_text[i] = upper_case_alphabet[cipher_key_index -1]
            else:
                cipher_key_index = (lower_case_alphabet.index(chars[i])+1 + rot) % len(lower_case_alphabet)
                cipher_text[i] = lower_case_alphabet[cipher_key_index - 1]
        # return "".join(cipher_text)
        self.set_message("".join(cipher_text))

    def decrypt_caesar(self):
        rot = sum([lower_case_alphabet.index(charKey.lower())+1 for charKey in self.key]) % len(lower_case_alphabet)
        plain_text = [""] * len(self.message)
        chars = [char for char in self.message]
        for i in range(len(chars)):
            if chars[i] is " ":
                plain_text[i] = " "
            elif chars[i].lower() != chars[i]:
                cipher_key_index = (upper_case_alphabet.index(chars[i])+1 + len(upper_case_alphabet) - rot) % len(upper_case_alphabet)
                plain_text[i] = upper_case_alphabet[cipher_key_index - 1]
            else:
                cipher_key_index = (lower_case_alphabet.index(chars[i])+1 + len(lower_case_alphabet) - rot) % len(lower_case_alphabet)
                plain_text[i] = lower_case_alphabet[cipher_key_index - 1]
        # return "".join(plain_text)
        self.set_message("".join(plain_text))

    """
    """"""""""""""""""AldenCipher""""""""""""""""""""
    """
