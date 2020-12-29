from src import Card
import random

# GLOBALS
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
card_dict = {'Two':2,
        'Three':3,
        'Four':4,
        'Five':5, 
        'Six':6,
        'Seven':7,
        'Eight':8,
        'Nine':9,
        'Ten':10,
        'Jack':10,
        'Queen':10, 
        'King':10, 
        'Ace':11}

class Deck:

    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def __str__(self):
        return [print(card) for card in self.deck]

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop()


