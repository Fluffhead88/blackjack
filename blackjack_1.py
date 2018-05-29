
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
        return self.hand

    def draw(self, deck):
        self.add(deck.draw())
        return self.hand


    def hit(self, deck):
        self.choice = input("Hit or Stand? ").lower()
        for choice in self.choice:
            if self.choice == "hit":
                self.draw(deck)
            else:
                break
            return self.hand_value()


    """def dealer_play(self):
        while self.player.hand_value() < 17:
            self.hand += self.player.hit()
            print(self.hand)
            if self.player.hand_value() < 17:
                self.hand += '' """



    def check(self):
        score = self.hand_value()
        if score > 21:
            print("Bust!")
        elif score == 21:
            print("Blackjack!")

    def hand_value(self):
        value = 0
        for card in self.hand:
            value += card.get_value()
        if value > 21 and "A" in self.hand:
            value -= 10
        return value

    """def __str__(self):
        return self.hand

    def __repr__(self):
        return Player(self.hand)"""


    """def __gt__(self, dealer):
        return self.hand_value() > dealer.hand_value()

    def __eq__(self, dealer):
        return self.hand_value() == dealer.hand_value()"""

"""class Dealer(Player):

    def __init__(self):
        self.hand = []

    def dealer_hit(self):
        if hand_value < 17:"""








print("Dealing cards")
deck = Deck()
#hand = Player()
#print (hand)
while True:
    input()
    player = Player()
    dealer = Player()

    for i in range(2):
        player.draw(deck)
        dealer.draw(deck)
    print(f"Player:{player.hand_value()}")
    print(f"Dealer:{dealer.hand_value()}")
    if player.hand_value() < 21:
        player.hit(deck)
        print(f"Player:{player.hand_value()}")
    player.check()
    input()
    while dealer.hand_value() < 17:
        dealer.draw(deck)
        print(f"Dealer:{dealer.hand_value()}")
    dealer.check()
    print(f"Player:{player.hand_value()}, Dealer:{dealer.hand_value()}")
    if player.hand_value() <= 21 and dealer.hand_value() <= 21 and dealer.hand_value() > player.hand_value():
        print("Dealer wins")
    elif player.hand_value() > 21 and dealer.hand_value() <= 21:
        print("Dealer wins")
    elif player.hand_value() <= 21 and dealer.hand_value() <= 21 and dealer.hand_value() < player.hand_value():
        print("You win!")
    elif player.hand_value() <= 21 and dealer.hand_value() < 21:
        print("You win!")
    elif player.hand_value() <= 21 and dealer.hand_value() <= 21 and dealer.hand_value() == player.hand_value():
        print("You tied")

    exit()
