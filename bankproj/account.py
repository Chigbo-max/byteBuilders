import random
from decimal import Decimal

class Account:
    def __init__(self, name= 'str', phone = '00000000000', pin = '0000', number = '0000000000') -> None:
        self.__name = name
        self.__phone = self.set_phone(phone)
        self.__pin = self.set_pin(pin)
        self.__balance = Decimal('0.00')
        self.__number = number

    def set_phone(self, phone):
        if len(phone) != 11:
            raise ValueError('Phone number must be 11-digits')
        self.__phone = phone
        return self.__phone

    def validate_balance(self, amount):
        self.validate_amount(amount)
        self.__balance = amount
        return self.__balance

    def validate_amount(self, amount):
        if amount < Decimal('0.00'):
            raise ValueError

    def deposit(self, amount):
        self.validate_amount(amount)
        self.__balance += amount


    def withdraw(self, amount, new_pin):
        self.validate_new_pin(new_pin)
        self.validate_amount(amount)
        if self.__balance < amount:
            raise ValueError('Insufficient balance')
        self.__balance -= amount

    def get_balance(self):
        return self.__balance

    def get_number(self):
        return self.__number

    def set_pin(self, pin):
        if len(pin) != 4:
            raise ValueError('Pin must be 4-digits')
        self.__pin = pin
        return self.__pin

    def set_new_pin(self, pin, new_pin):
        if pin == self.__pin:
            self.__pin = new_pin
        else:
            raise ValueError('Pin does not match')

    def validate_new_pin(self, new_pin):
        if len(new_pin) != 4:
            raise ValueError('Pin must be 4-digits')







