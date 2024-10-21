import unittest
import listsorting

class TestListSorting(unittest.TestCase):
	def test_that_display_ascending_order_function_exist(self):
		listsorting.display_ascending_order
		
	def test_that_display_ascending_order_function_returns_ascending_numbers(self):
		numbers = [5, 2, 7, 2, 8, 2, 3, 4, 6]
		expected = [2, 2, 2, 3, 4, 5, 6, 7, 8]
		self.assertEqual(listsorting.display_ascending_order(numbers), expected)

	def test_that_display_ascending_order_function_raise_errors_for_invalid_string_values(self):
		self.assertRaises(TypeError, listsorting.display_ascending_order, "ewee")




	def test_that_display_descending_order_function_exist(self):
		listsorting.display_descending_order
		
	def test_that_display_descending_order_function_returns_descending_numbers(self):
		numbers = [5, 2, 7, 2, 8, 2, 3, 4, 6]
		expected = [8, 7, 6, 5, 4, 3, 2, 2, 2]
		self.assertEqual(listsorting.display_descending_order(numbers), expected)

	def test_that_display_descending_order_function_raise_errors_for_invalid_string_values(self):
		self.assertRaises(TypeError, listsorting.display_descending_order, "ewee")





	def test_that_display_multiplication_of_elements_at_third_positions_function_exist(self):
		listsorting.display_multiplication_of_elements_at_third_positions
		
	def test_that_display_multiplication_of_elements_at_third_positions_function_returns_the_product(self):
		numbers = [8, 7, 6, 5, 4, 3, 2, 2, 2]
		expected = 36
		self.assertEqual(listsorting.display_multiplication_of_elements_at_third_positions(numbers), expected)





	def test_that_display_squared_elements_function_exist(self):
		listsorting.display_squared_elements
		
	def test_that_display_squared_elements_function_returns_the_product(self):
		numbers = [8, 7, 6, 5, 4, 3, 2, 2, 2]
		expected = [64, 49, 36, 25, 16, 9, 4, 4, 4]
		self.assertEqual(listsorting.display_squared_elements(numbers), expected)

	def test_that_display_squared_elements_function_raise_errors_for_invalid_string_values(self):
		self.assertRaises(TypeError, listsorting.display_squared_elements, "ewee")


	def test_that_display_squared_elements_function_raise_errors_for_negative_values(self):
		self.assertRaises(ValueError, listsorting.display_squared_elements, -1)

