import unittest
import dollartonaira

#from unittest, import TestCase
#import dollartonaira, import divideorsquare

class TestDollarToNaira(unittest.TestCase):
	def test_that_convert_dollar_to_naira_function_exist(self):
		dollartonaira.convert_dollar_to_naira(3)

	def test_that_convert_dollar_to_naira_function_returns_correct_value_with_floating_values(self):
		self.assertEqual(round(dollartonaira.convert_dollar_to_naira(20.1)), 31_155)
		self.assertEqual(dollartonaira.convert_dollar_to_naira(35.25), 54637.5)
	
	def test_that_convert_dollar_to_naira_function_raises_error_for_negative_values(self):
		self.assertRaises(ValueError, dollartonaira.convert_dollar_to_naira, -1)
	
	def test_that_convert_dollar_to_naira_function_raises_error_for_string_values(self):
		self.assertEqual(dollartonaira.convert_dollar_to_naira("kudi"), "Invalid input")
		self.assertEqual(dollartonaira.convert_dollar_to_naira(""), "Invalid input")

#class TestDivideorSquare(TestCase):
	#def test_that_divide_or_square_function_exist(self):
		#divideorsquare.divide_or_square(3)