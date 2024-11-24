from decimal import Decimal

class Account:
    def __init__(self, name= 'str', phone = '00000000000') -> None:
        self.name = name
        self.phone = self.set_phone(phone)
        self.balance = Decimal('0.00')

    def set_phone(self, phone):
        if(len(phone) != 11):
            raise ValueError('Phone number must be 11-digit.')
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


    def withdraw(self, amount):
        self.validate_amount(amount)
        if self.balance < amount:
            raise ValueError
        self.balance -= amount

    def get_balance(self):
        return self.balance




