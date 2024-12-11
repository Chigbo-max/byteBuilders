import random
from account import Account
from decimal import Decimal



class Bank:


    def __init__(self, bank_name, bank_id) -> None:
        self.__id = bank_id
        self.bank_name = bank_name
        self.accounts = []

    def create_account(self, first_name, last_name, phone, pin):
        account_number = self.generate_account_number()
        name = first_name + " " + last_name
        new_account = Account(name, phone, pin, account_number)
        self.accounts.append(new_account)

    def get_bank_id(self):
        return self.__id

    def generate_account_number(self):
        account_number = str(random.randrange(1_200_000_000, 1_299_999_999))
        return account_number

    def deposit(self, account_number, amount):
        account = self.find_account(account_number)
        account.deposit(amount)

    def find_account(self, account_number):
        for account in self.accounts:
            if account.get_number() == account_number:
                return account
        raise ValueError('Account number does not match')

    def withdraw(self, account_number, amount, pin ):
        account = self.find_account(account_number)
        account.withdraw(amount,pin)


    def transfer(self, sender_account_number, recipient_account_number, amount, pin):
        account1 = self.find_account(sender_account_number)
        account2 = self.find_account(recipient_account_number)
        account1.validate_new_pin(pin)
        account2.deposit(amount)
        account1.withdraw(amount,pin)


    def validate_account_number(self, acc_number):
        if len(acc_number) != 10:
            raise ValueError('Account number must be 10-digits')


