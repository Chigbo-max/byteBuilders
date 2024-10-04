import unittest
import multiplication


class Multiplication(unittest.TestCase):
	def test_that_display_multiplication_fuction_exist(self):
		multiplication.display_multiplication(1, 2)

	def test_that_display_multiplication_fuction_returns_correct_value_with_floating_values(self):
		multiplication.display_multiplication((3.2,2), 6.4)

	def test_that_display_multiplication_fuction_returns_correct_value_with_negative_values(self):
		multiplication.display_multiplication((3.2,-2), -6.4)
		multiplication.display_multiplication((-3.2,-2), 6.4)


	def test_that_display_multiplication_fuction_raise_errors_for_invalid_string_values(self):
		self.assertRaises(TypeError, multiplication.display_multiplication, "wawu")





	
