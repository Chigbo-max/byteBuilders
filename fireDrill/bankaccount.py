import random
from decimal import Decimal

class Account:
    def __init__(self, name= 'str', phone = '00000000000', pin = '0000') -> None:
        self.name = name
        self.phone = self.set_phone(phone)
        self.pin = self.set_pin(pin)
        self.balance = Decimal('0.00')
        self.account_number = self.generate_account_number()

    def set_phone(self, phone):
        if len(phone) != 11:
            raise ValueError('Phone number must be 11-digits')
        self.phone = phone
        return self.phone

    def validate_balance(self, amount):
        self.validate_amount(amount)
        self.balance = amount
        return self.balance

    def validate_amount(self, amount):
        if amount < Decimal('0.00'):
            raise ValueError

    def deposit(self, amount):
        self.validate_amount(amount)
        self.balance += amount


    def withdraw(self, amount, acc_number, new_pin):
        self.validate_account_number(acc_number)
        self.new_pin(new_pin)
        self.validate_amount(amount)
        if self.balance < amount:
            raise ValueError
        self.balance -= amount

    def get_balance(self):
        return self.balance

    def generate_account_number(self):
        account_number = str(random.randrange(1_200_000_000, 1_299_999_999))
        return account_number

    def get_account_number(self):
        return self.account_number

    def validate_account_number(self, acc_number):
        if len(acc_number) != 10:
            raise ValueError('Account number must be 10-digits')

    def set_pin(self, pin):
        if len(pin) != 4:
            raise ValueError('Pin must be 4-digits')
        self.pin = pin
        return self.pin

    def set_new_pin(self, pin, new_pin):
        if pin == self.pin:
            self.pin = new_pin
        else:
            raise ValueError('Pin does not match')

    def new_pin(self, new_pin):
        if len(new_pin) != 4:
            raise ValueError('Pin must be 4-digits')
        self.pin = new_pin




