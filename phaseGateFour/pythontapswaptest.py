import unittest
import pythontapswap

class TestArraySwap(unittest.TestCase):
	def test_that_get_swapped_elements_function_exist(self):
		pythontapswap.get_swapped_elements([0, 0, 0, 0, 0, 0])
	
	def test_that_get_swapped_elements_function_returns_swapped_elements(self):
		numbers = [1, 2, 3, 4, 5, 6]
		expected = [2, 1, 4, 3, 6, 5]
		self.assertEqual(pythontapswap.get_swapped_elements(numbers), expected)