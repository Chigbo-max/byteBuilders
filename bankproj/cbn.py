from bank import Bank


class Cbn:
    def __init__(self):
        self.banks = []

    def create_bank(self, bank_name):
        __id = len(self.banks) + 1
        new_bank = Bank(bank_name, __id)
        self.banks.append(new_bank)
        return new_bank


    def transfer(self, sender_bank_id, recipient_bank_id, sender_account_number, recipient_account_number, amount, pin):
        sending_bank = self.find_bank(sender_bank_id)
        receiving_bank = self.find_bank(recipient_bank_id)

        sending_bank.find_account(sender_account_number)
        receiving_bank.find_account(recipient_account_number)

        receiving_bank.deposit(recipient_account_number, amount)
        sending_bank.withdraw(sender_account_number, amount, pin)



    def find_bank(self, bank_id)-> Bank:
        for found_bank in self.banks:
            if found_bank.get_bank_id() == bank_id:
                return found_bank
        raise ValueError("bank not found")