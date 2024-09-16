import unittest
import palindromicnumber

class PalindromicNumber(unittest.TestCase):
	def test_that_the_prime_number_function_exist(self):
		palindromicnumber.prime_number(345)
	
	def test_that_the_prime_number_function_determines_a_prime_number(self):
		self.assertIs(palindromicnumber.prime_number(11), True)
		self.assertIs(palindromicnumber.prime_number(10), False)
	
	def test_that_the_palindrome_function_exist(self):
		palindromicnumber.palindrome_number(111)
	
	def test_that_the_palindrome_function_returns_a_palindrome(self):
		self.assertIs(palindromicnumber.palindrome_number(11), True)
		self.assertIs(palindromicnumber.palindrome_number(98), False)

	def test_that_palindromic_number_function_exist(self):
		palindromicnumber.palindromic_number(121)
	
	def test_that_palindromic_number_function_returns_true_or_false_if_number_is_palindromic(self):
		self.assertIs(palindromicnumber.palindromic_number(11),True)

	def test_that_palindromic_number_function_raises_error_for_negative_values(self):
		self.assertRaises(ValueError, palindromicnumber.palindromic_number, -1)

	def test_that_palindromic_number_function_raises_error_for_string_values(self):
		self.assertRaises(TypeError, palindromicnumber.palindromic_number, "agbado")