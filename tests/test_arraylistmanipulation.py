import unittest
from fireDrill import arraylistmanipulation


class ArrayListManipulationTestCase(unittest.TestCase):
    def test_add_third_elements_function_exist(self):
        arraylistmanipulation.add_third_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    def test_that_add_third_elements_function_adds_third_elements_into_an_array_list(self):
        actual = arraylistmanipulation.add_third_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        expected = 18
        self.assertEqual(actual, expected)

    def test_that_add_third_elements_function_throws_exception_for_string(self):
        self.assertRaises(TypeError, arraylistmanipulation.add_third_elements([1, 2, 3, 'a', 5, 6, 7, 8, 9, 10]))

    def test_that_sum_first_middle_and_last_element_function_exist(self):
        arraylistmanipulation.sum_first_middle_and_last_element([1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_that_sum_first_middle_and_last_element_function_returns_expected_result(self):
        actual = arraylistmanipulation.sum_first_middle_and_last_element([1, 2, 3, 4, 5, 6, 7, 8, 9])
        expected = 15
        self.assertEqual(actual, expected)

    def test_that_sum_first_middle_and_last_element_function_raises_exception_for_string(self):
        self.assertRaises(TypeError, arraylistmanipulation.sum_first_middle_and_last_element([1, 2, 'a', 4, 5, 6, 7, 8, 9]))

