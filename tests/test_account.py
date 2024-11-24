import unittest
from fireDrill import account
from fireDrill.account import Account


class MyTestCase(unittest.TestCase):
    def test_deposit_5h_get_balance_5h(self):
        chigbo_account = Account()
        self.assertEqual(0, chigbo_account.get_balance())
        chigbo_account.deposit(500)
        self.assertEqual(500, chigbo_account.get_balance())

    def test_deposit_5h_twice_get_balance_1k(self):
        chigbo_account = Account()
        self.assertEqual(0, chigbo_account.get_balance())
        chigbo_account.deposit(500)
        chigbo_account.deposit(500)
        self.assertEqual(1000, chigbo_account.get_balance())

    def test_withdraw_5h_get_balance_5h(self):
        chigbo_account = Account()
        chigbo_account.deposit(1000)
        chigbo_account.withdraw(500)
        self.assertEqual(500, chigbo_account.get_balance())

    def test_withdraw_50_100_get_balance_50_000_where_current_balance_is_50_000(self):
        chigbo_account : Account = Account()
        chigbo_account.deposit(50_000)
        chigbo_account.withdraw(50_100)
        self.assertEqual(50_000, chigbo_account.get_balance())

    def test_withdraw_negative_500_get_balance_zero_when_balance_is_zero(self):
        chigbo_account = Account()
        chigbo_account.deposit(0)
        chigbo_account.withdraw(-500)
        self.assertEqual(0, chigbo_account.get_balance())


