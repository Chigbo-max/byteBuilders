import unittest

import rot13cipher
from rot13cipher import encrypt_text


class RotCipherCase(unittest.TestCase):

    def testThatEncryptedTextIsReturned(self):
        text = 'H'
        actual = encrypt_text(text)
        expected = 'U'
        print(actual)
        self.assertEqual(actual, expected)

    def testThatEncryptedStringIsRetrurned(self):
        string = "Hello"
        actual = encrypt_text(string)
        expected = "Uryyb"
        print(actual)
        self.assertEqual(actual, expected)






