import unittest
import divideorsqaure

class TestDivideOrSquare(unittest.TestCase):
	def test_that_divide_or_square_function_exist(self):
		divideorsqaure.divide_or_square(300)

	def test_that_divide_or_square_function_returns_decimal_values(self):
		self.assertEqual(divideorsqaure.divide_or_square(10), 3.16)

	def test_that_divide_or_square_function__raises_error_for_string_values(self):
		self.assertRaises(TypeError, divideorsqaure.divide_or_square("mmm"), "Invalid input")








































