import unittest
import onlyfloats

class OnlyFloats(unittest.TestCase):
	def test_that_only_floats_function_exist(self):
		onlyfloats.only_floats(1,2)

	def test_that_function_returns_two_if_both_numbers_are_floats_or_one_if_either_is_a_float_or_zero_if_none_is_float(self):
		self.assertEqual(onlyfloats.only_floats(0.1, 0.1),2)
		self.assertEqual(onlyfloats.only_floats(0.1, 1), 1)
		self.assertEqual(onlyfloats.only_floats(1, 2), 0)
	
	def test_that_function_raise_errors_with_negative_values(self):
		self.assertRaises(ValueError, onlyfloats.only_floats, -1, -1)

	def test_that_function_raise_errors_with_string_values(self):
		self.assertRaises(TypeError, onlyfloats.only_floats, "aboki")
	
