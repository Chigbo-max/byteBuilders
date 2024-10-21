import unittest
import generatepassword
import string
import random

class TestPasswordGenerator(unittest.TestCase):
	def test_that_generate_password_function_exist(self):
		generatepassword.generate_password()
	
	def test_that_generate_password_function_returns_characters_greater_than_or_equal_to_sixteen(self):

		self.assertTrue(generatepassword.generate_password, 17)
		
	def test_that_generate_password_function_contains_upper_case(self):
		
		array = generatepassword.generate_password()

		self.assertTrue(any(count for count in array if count in string.ascii_uppercase))


	def test_that_generate_password_function_contains_lowercase_case(self):
		
		array = generatepassword.generate_password()

		self.assertTrue(any(count for count in array if count in string.ascii_lowercase))


	def test_that_generate_password_function_contains_digits(self):
		
		array = generatepassword.generate_password()

		self.assertTrue(any(count for count in array if count in string.digits))


	def test_that_generate_password_function_contains_character(self):
		
		array = generatepassword.generate_password()

		self.assertTrue(any(count for count in array if count in string.punctuation))
		
		
