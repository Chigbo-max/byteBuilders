import unittest

from bankproj.bank import Bank
from bankproj.account import Account


class TestBank(unittest.TestCase):
    def test_that_two_accounts_are_registered(self):
        fidelity = Bank()
        account_1 = fidelity.create_account("Guy","Slate","09089756312", "1234")
        fcmb = Bank()
        account_2 = fcmb.create_account("easy","farabale","09032456789","1212")
        self.assertEqual(fcmb.get_number_of_accounts(), 2)  # add assertion here


    def test_that_deposit_2k_get_2k_balance_works(self ):
        fidelity_bank = Bank()
        account1 = fidelity_bank.create_account("Guy","Slate","09089756312", "1234")
        fidelity_bank.deposit(account1.get_number(),2000)
        self.assertEqual(fidelity_bank.get_balance((account1.get_number())),2000)

    def test_that_deposit_10k_withdraw_2k_get_8k_balance_works(self ):
        fidelity_bank = Bank()
        account1 = fidelity_bank.create_account("Guy","Slate","09089756312", "1234")
        fidelity_bank.deposit(account1.get_number(), 10000)
        fidelity_bank.withdraw(account1.get_number(), 2000, "1234")
        self.assertEqual(fidelity_bank.get_balance(account1.get_number()), 8000)

    def test_that_transfer_of_8k_works_get_2k_balance(self):
        fidelity_bank = Bank()
        account1 = fidelity_bank.create_account("Guy","Slate","09089756312", "1234")
        fidelity_bank.deposit(account1.get_number(), 10000)

        account2 = fidelity_bank.create_account("easy", "radiant","09033412345", "1234")
        fidelity_bank.transfer(account1.get_number(), account2.get_number(), 8000, "1234")
        self.assertEqual(fidelity_bank.get_balance(account1.get_number()), 2000)

    def test_that_error_is_raised_if_pin_does_not_match(self):
        fidelity_bank = Bank()
        account1 = fidelity_bank.create_account("Guy", "Slate", "09089756312", "1234")
        fidelity_bank.deposit(account1.get_number(), 10000)

        account2 = fidelity_bank.create_account("easy", "radiant", "09033412345", "1234")
        self.assertRaises(Exception, fidelity_bank.transfer, account1.get_number(), account2.get_number(), 2000, 111)

    def test_that_error_is_thrown_if_account_number_does_not_match(self ):
        fidelity_bank = Bank()
        fidelity_bank.create_account("Guy","Slate","09089756312", "1234")
        fcmb = Bank()
        fcmb.create_account("easy", "radiant","09033412345", "1234")
        self.assertRaises(Exception, fidelity_bank.transfer, "0000000000", 2000)