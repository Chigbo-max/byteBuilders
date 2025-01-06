from unittest import TestCase
from src.calculation import Calculation

class TestCalculation(TestCase):
    def  test_that_exception_is_thrown_for_negative_interest_rate(self):
        interest_rate = -5
        compound_frequency = 5
        time = 10
        self.assertRaises(Exception, Calculation.get_interest_factor_result, interest_rate, compound_frequency, time)

