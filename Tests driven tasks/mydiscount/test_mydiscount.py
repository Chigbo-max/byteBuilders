import unittest
import mydiscount

class MyDiscount(unittest.TestCase):
	def test_that_function_my_discount_exist(self):
		mydiscount.my_discount(1, 2)
	
	def test_that_function_my_discount_returns_the_new_price_after_discount(self):
		self.assertEqual(mydiscount.my_discount(100, 5), 100-5)

	def test_that_function_my_discount_raise_errors_for_invalid_numbers(self):
		self.assertRaises(ValueError, mydiscount.my_discount, -1, -1)

	def test_that_function_my_discount_raise_errors_for_invalid_string_values(self):
		self.assertRaises(TypeError, mydiscount.my_discount, "wawu")

