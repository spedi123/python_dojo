from classes.deck import Deck


class Player:
    def __init__(self, name):
        self.name = name
        self.is_bursted = False
        self.sum = 0
        self.hands = []


bicycle = Deck()

bicycle.show_cards()
