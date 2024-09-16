import unittest
import futureinvestment

class FutureInvestment(unittest.TestCase):
	def test_that_future_investment_function_exist(self):
		futureinvestment.future_investment(3,2,1)

	def test_that_future_investment_function_returns_the_number_of_months(self):
		self.assertEqual(futureinvestment.future_investment(3, 2, 1), 3*(1+0.02)**(1*12))
		self.assertEqual(futureinvestment.future_investment(3, 2, 0), 3*(1+0.02)**(0*12))
		self.assertEqual(futureinvestment.future_investment(3, 2, 2), 3*(1+0.02)**(2*12))

	def test_that_future_investment_function_returns_the_future_investment_value(self):
		self.assertEqual(futureinvestment.future_investment(3,2,3), 3*(1+0.02)**(3*12))
	
	def test_that_future_investment_function_raise_error_with_negative_values(self):
		self.assertRaises(ValueError, futureinvestment.future_investment, -1, -1, -1)

	def test_that_future_investment_function_raise_error_with_string_value(self):
		self.assertRaises(TypeError, futureinvestment.future_investment, "dele")