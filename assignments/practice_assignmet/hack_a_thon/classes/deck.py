from . import card
import random


class Deck:

    def __init__(self):
        suits = ["spades", "hearts", "clubs", "diamonds"]
        self.cards = []

        for s in suits:
            for i in range(1, 14):
                str_val = ""
                if i == 1:
                    str_val = "Ace"
                elif i == 11:
                    str_val = "Jack"
                    point_val = 10
                elif i == 12:
                    str_val = "Queen"
                    point_val = 10
                elif i == 13:
                    str_val = "King"
                    point_val = 10
                else:
                    str_val = str(i)
                self.cards.append(card.Card(s, point_val, str_val))

    def show_cards(self):
        for card in self.cards:
            card.card_info()

    def shuffle_cards(self):
        random.shuffle(self.cards)

    def draw(self):
        draw_game = self.cards.pop(0)
        return draw_game
