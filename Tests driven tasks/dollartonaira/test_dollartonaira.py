import unittest
import dollartonaira

class TestDollarToNaira(unittest.TestCase):
	def test_that_dollar_to_naira_function_exist(self):
		dollartonaira.dollar_to_naira(3)

	def test_that_user_enters_a_number(self):
		self.assertEqual(dollartonaira.dollar_to_naira(1), 1550.0)
	
	def test_that_dollar_to_naira_function_raises_error_for_negative_values(self):
		self.assertRaises(ValueError, dollartonaira.dollar_to_naira, 0)
	
	def test_that_dollar_to_naira_function_raises_error_for_string_values(self):
		self.assertRaises(TypeError, dollartonaira.dollar_to_naira, "kudi")