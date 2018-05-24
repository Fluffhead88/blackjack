
import random

class Card:

    def __init__(self, value): #add suit
        self.value = value # need suits in blackjack
        #self.suit = suit

class Deck:

    def __init__(self): # creates range of cards and shuffles
        self.cards =[]

        for value in range(2, 10):
            self.cards.append(Card(value))

        for value in range(11,13):
            value = 10
            self.cards.append(Card(value))
        for value in range(14,14):
            value = 11
        self.cards.append(Card(value))

        random.shuffle(self.cards)

    def draw(self): # takes off cards for use somewhere else
        return self.cards.pop()

    def __str__(self): # shows you cards
        for card in self.cards:
            print(card.value)
        return ""

class Player:

    def __init__(self):
        self.hand= []

    def add(self, card):
        self.hand.append(card)

    def draw_from_deck(self, deck):
        self.add(deck.draw())


    def hit(self):
        self.choice = input("Hit (Y/N)? ").lower
        while self.choice == "y":
            self.draw_from_deck()
        return self.hand_value()

    def bust(self):
        score = self.hand_value()
        if score > 21:
            print("Bust!")
            pass

    def get_blackjack(self):
        score = self.hand_value()
        if score == 21:
            print("Blackjack!")

    def hand_value(self):
        value = 0
        for card in self.hand:
            value += card.value
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
    player_1.hit()
    player_1.bust()
    player_1.get_blackjack()
    print("Player 2")
    player_2.hit()
    player_2.bust()
    player_2.get_blackjack()
    print(f"Player One:{player_1.hand_value()}")
    print(f"Player Two:{player_2.hand_value()}")
