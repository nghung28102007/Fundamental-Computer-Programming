class CreditCard:
    def __init__(self, number, cvv, expiry):
        self.number = number 
        self.cvv = cvv
        self.expiry = expiry
    class User:
        def __init__(self, name):
            self.name = name
            self.cards = []

        def add_card(self, card):
            self.cards.append(card)

card1 = CreditCard("hung", '0846281007', '01234567',)
    