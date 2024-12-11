import unittest

from bankproj.bank import Bank


class TestBank(unittest.TestCase):
    def test_that_two_banks_are_regitered(self):
        fidelity_bank = Bank()
        fidelity_bank.create_account("Guy","Slate","09089756312", "1234")
        fcmb = Bank()
        fcmb.create_account("easy","farabale","09032456789","1212")
        self.assertEqual(fcmb.get_number_of_accounts(), 2)  # add assertion here



