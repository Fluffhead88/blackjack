
import random

class Card:

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def get_value(self):
        if self.value == 'J':
            return 10
        if self.value == 'Q':
            return 10
        if self.value == 'K':
            return 10
        if self.value == 'A':
            return 11

        return self.value


class Deck:

    def __init__(self): # creates range of cards and shuffles
        self.cards =[]

        values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
        suits = ['Clubs', 'Spades', 'Hearts', 'Diamonds']

        for value in values:
            for suit in suits:
                self.cards.append(Card(value, suit))

        random.shuffle(self.cards)

    def draw(self): # takes off cards for use somewhere else
        return self.cards.pop()

    def __str__(self): # shows you cards
        for card in self.cards:
            print(card.value, card.suit)
        return ""

class Player:

    def __init__(self):
        self.hand= []

    def add(self, card):
        self.hand.append(card)

    def draw_from_deck(self, deck):
        self.add(deck.draw())



    def hit(self, deck):
        self.choice = input("Hit (Y/N)? ").lower()
        if self.choice == "y":
            self.draw_from_deck(deck)
        return self.hand_value()

    def bust(self):
        score = self.hand_value()
        if score > 21:
            print("Bust!")


    def get_blackjack(self):
        score = self.hand_value()
        if score == 21:
            print("Blackjack!")

    def hand_value(self):
        value = 0
        for card in self.hand:
            value += card.get_value()
        return value


deck = Deck()
print (deck)

while True:
    input()

    player_1 = Player()
    player_2 = Player()
    player_1.draw_from_deck(deck)
    player_1.draw_from_deck(deck)
    player_2.draw_from_deck(deck)
    player_2.draw_from_deck(deck)
    print(f"Player One:{player_1.hand_value()}")
    print(f"Player Two:{player_2.hand_value()}")
    print("Player 1")
    player_1.hit(deck)
    player_1.bust()
    player_1.get_blackjack()
    print("Player 2")
    player_2.hit(deck)
    player_2.bust()
    player_2.get_blackjack()
    print(f"Player One:{player_1.hand_value()}")
    print(f"Player Two:{player_2.hand_value()}")
