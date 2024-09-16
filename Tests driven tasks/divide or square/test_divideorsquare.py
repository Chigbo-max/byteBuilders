import unittest
import divideorsquare

class TestDivideOrSquare(unittest.TestCase):
	def test_that_divide_or_square_function_exist(self):
		 divideorsquare.divide_or_square(25)
	
	def test_that_divide_or_square_function_returns_the_square_root_of_a_number_if_divisible_by_five(self):
		self.assertEqual(divideorsquare.divide_or_square(25),(25**0.5))
		self.assertEqual(divideorsquare.divide_or_square(4), 4 % 5)
		self.assertEqual(divideorsquare.divide_or_square(26), 26 % 5)
		self.assertEqual(divideorsquare.divide_or_square(0), 0 % 5)

	def test_that_divide_or_square_function_raise_error_with_negative_number(self):
		self.assertRaises(ValueError, divideorsquare.divide_or_square, -1)
	
	def test_that_divide_or_square_function_raise_error_with_string_value(self):
		self.assertRaises(TypeError, divideorsquare.divide_or_square, "byte")



	