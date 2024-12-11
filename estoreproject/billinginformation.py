from address import Address
from creditcardinformation import CreditCardInformation


class BillingInformation():
    def __init__(self, receiver_phone_number, receiver_name,  street, state, city_name, house_number, country_name, card_cvv, card_expiration_month, card_expiration_year, credit_card_number,name_on_card):
        self.receiver_phone_number = receiver_phone_number
        self.receiver_name = receiver_name
        self.delivery_address = Address(street, state, city_name, house_number, country_name)
        self.credit_card_information = CreditCardInformation(card_cvv, card_expiration_month, card_expiration_year, credit_card_number,name_on_card)