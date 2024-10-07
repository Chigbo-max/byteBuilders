import unittest
import stringinteger

class TestStringInteger(unittest.TestCase):
	def test_that_string_integer_function_exist(self):
		stringinteger.string_integer(23, 44)

	def test_that_string_integer_function_returns_sum_of_two_integer_values(self):
		self.assertEqual(stringinteger.string_integer('3','2'), '5')
	
	def test_that_string_integer_function_returns_string_values(self):
		self.assertEqual(stringinteger.string_integer('3', '2'), '5')	
