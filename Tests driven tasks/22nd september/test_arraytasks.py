import unittest
import arraytasks

class TestArrayTasks(unittest.TestCase):
	def test_that_display_largest_element_function_exist(self):
		arraytasks.display_largest(300)
	
	def test_that_display_largest_element_function_returns_largest_element(self):
		self.assertEqual(arraytasks.display_largest([1,2,3,4,5,6]), 6)

	def test_that_display_largest_element_function_raises_error_for_empty_list(self):
		self.assertRaises(ValueError, arraytasks.display_largest, [])

class TestReverse(unittest.TestCase):
	def test_that_display_reverse_function_exist(self):
		arraytasks.display_reverse(2)
	
	def test_that_reverse_function_returns_reverse(self):
		self.assertEqual(arraytasks.display_reverse([1,2,3,4,5]), [5,4,3,2,1])

	def test_that_reverse_function_raises_error_for_empty_list(self):
		self.assertRaises(ValueError, arraytasks.display_reverse, [])

class TestElementOccurence(unittest.TestCase):
	def test_that_display_number_occurence_check_function_exists(self):
		arraytasks.display_number_occurence_check(1)

	def test_that_an_element_occurs_in_a_list(self):
		self.assertEqual(arraytasks.display_number_occurence_check([1,2,3,4,5]), 3)
	
	def test_that_display_number_occurence_check_function_raises_error_for_empty_list(self):
		self.assertRaises(ValueError, arraytasks.display_reverse, [])

class TestElementsOnOddPositions(unittest.TestCase):
	def test_that_display_odd_elements_function_exits(self):
		arraytasks.display_odd_elements(4)

	def test_that_display_odd_elements_function_returns_odd_elements(self):
		self.assertEqual(arraytasks.display_odd_elements([1,2,3,4,5]), 2,4)
	
	def test_that_display_odd_elements_function_raises_error_for_empty_list(self):
		self.assertRaises(ValueError, arraytasks.display_odd_elements, [])

class TestElementsOnEvenPositions(unittest.TestCase):
	def test_that_display_even_elements_function_exits(self):
		arraytasks.display_even_elements(4)

	def test_that_display_even_elements_function_returns_even_elements(self):
		self.assertEqual(arraytasks.display_even_elements([1,2,3,4,5]), 1,3,)
	
	def test_that_display_even_elements_function_raises_error_for_empty_list(self):
		self.assertRaises(ValueError, arraytasks.display_even_elements, [])

class TestRunningTotal(unittest.TestCase):
	def test_that_display_running_total_function_exists(self):
		arraytasks.display_running_total(3)

	def test_that_display_running_total_function_return_running_total(self):
		self.assertEqual(arraytasks.display_running_total([1,2,3,4,5]), 1, 3,)

class TestPalindrome(unittest.TestCase):
	def test_that_display_string_palindrome_function_exists(self):
		arraytasks.display_string_palindrome(4)

	def test_that_display_string_palindrome_function_returns_palindrome(self):
		self.assertEqual(('abcde'), 'ed')