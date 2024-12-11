from cardtype import CardType


class CreditCardInformation():
    def __init__(self, card_cvv, card_expiration_month, card_expiration_year, credit_card_number,name_on_card):
        self.card_cvv = card_cvv
        self.card_expiration_month = card_expiration_month
        self.card_expiration_year = card_expiration_year
        self.credit_card_number = credit_card_number
        self.name_on_card = name_on_card
        self.MASTER_CARD = CardType.MASTER_CARD
        self.VISA_CARD = CardType.VISA_CARD
        self.VERVE = CardType.VERVE
        self.AMERICA_EXPRESS = CardType.AMERICA_EXPRESS
