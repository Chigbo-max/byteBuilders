class Account:

    def __init__(self):
        self._balance = 0

    def get_balance(self)->int:
        return self._balance

    def deposit(self, amount:int)->None:
        self._balance += amount

    def withdraw(self, amount:int)->None:
        self.withdraw_amount_greater_than_balance(amount)

    def withdraw_amount_greater_than_balance(self, amount:int)->int:
        if self._balance == 0 and amount < self._balance:
            return 0
        if amount > self._balance:
            return self._balance
        self._balance -= amount

