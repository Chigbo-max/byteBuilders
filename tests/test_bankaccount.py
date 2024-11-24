import unittest
from fireDrill.bankaccount import Account
from decimal import Decimal

class TestBankAccount(unittest.TestCase):

    def setUp(self):
        self.tunde = Account("tunde", "09012345643")

    def test_that_account_exist(self):
        account1 = Account("tunde", "08012323412")
        account2 = Account("alex","09012345643")
        account3 = Account("lee")


    def test_that_balance_cannot_be_negative(self):

        self.assertRaises(ValueError, self.tunde.deposit, Decimal("-1200"))

    def test_that_balance_can_deposit(self):
        self.tunde.deposit(Decimal("1200.00"))
        # self.assertEqual(self.tunde.balance, Decimal("0.00"))
        # self.tunde.deposit(Decimal("1200.00"))
        self.assertEqual(self.tunde.get_balance(), Decimal("1200.00"))

    def test_that_account_cannot_deposit_negative_amount(self):

        self.assertEqual(self.tunde.get_balance(), Decimal("0.00"))
        self.assertRaises(ValueError, self.tunde.deposit, Decimal("-1200.00"))

    def test_that_balance_can_withdraw(self):
        self.assertEqual(self.tunde.get_balance(), Decimal("0.00"))
        self.tunde.deposit(Decimal("1200.00"))
        self.assertEqual(self.tunde.get_balance(), Decimal("1200.00"))

        self.tunde.withdraw(Decimal("1000.00"))
        self.assertEqual(self.tunde.get_balance(), Decimal("200.00"))

    def test_that_account_cannot_withdraw_negative_amount(self):
        self.assertEqual(self.tunde.get_balance(), Decimal("0.00"))
        # self.tunde.deposit(Decimal("1200.00"))
        # self.assertEqual(self.tunde.get_balance(), Decimal("1200.00"))
        # self.tunde.withdraw(Decimal("2000.00"))
        self.assertRaises(ValueError, self.tunde.withdraw, Decimal("-800.00"))




