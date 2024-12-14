import unittest
import encryptionanddecryption



class EncryptionAndDecryptionTestCase(unittest.TestCase):


    def testThat5Modulus26Returns5(self):
        number = 5
        actual = encryptionanddecryption.returnTheModulus(number)
        expected = 8
        self.assertEqual(actual, expected)

    def testThatDigitsAreIgnored(self):
        plain_text = "CALI12345A"
        actual = encryptionanddecryption.getValueOfCharacter(plain_text)
        expected = [2, 0, 11, 8, 0]
        self.assertEqual(actual, expected)

    def testThatTheNumericValueForCharacterIsReturned(self):
        plain_text = "CALIFORNIA"
        actual = encryptionanddecryption.getValueOfCharacter(plain_text)
        expected = [2, 0, 11, 8, 5, 14, 17, 13, 8, 0]
        self.assertEqual(actual, expected)

    def testThatTheEncryptedModulus26ValueForCharacterIsReturned(self):
        plain_text = "CALIFORNIA"
        actual =encryptionanddecryption.getEncryptedModulusValue(plain_text)
        expected = [5, 3, 14, 11, 8, 17, 20, 16, 11, 3]
        self.assertEqual(actual, expected)

    def testThatModulusValueReturnsTheEncryptedValue(self):
        plain_text = "CALIFORNIA"
        actual = encryptionanddecryption.getEncryptedResult(plain_text)
        expected = ['f', 'd', 'o', 'l', 'i', 'r', 'u', 'q', 'l', 'd']
        self.assertEqual(actual, expected)


    def testThatTheDecryptedModulus26ValueForCharacterIsReturned(self):
        plain_text = "CALIFORNIA"
        actual = encryptionanddecryption.getDecryptedModulusValue(plain_text)
        expected = [25, 23, 8, 5, 2, 11, 14, 10, 5, 23]
        self.assertEqual(actual, expected)

    def testThatModulusValueReturnsTheDecryptedValue(self):
        plain_text = "CALIFORNIA"
        actual = encryptionanddecryption.getDecryptedResult(plain_text)
        expected = ['z', 'x', 'i', 'f', 'c', 'l', 'o', 'k', 'f','x']
        self.assertEqual(actual, expected)


