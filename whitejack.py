import random
import os
import time


suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight',
         'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8,
          'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

playing = True


class Card:
    """
    Creates the cards
    """
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + ' of ' + self.suit


class Deck:
    """
    Creates the deck
    """
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def __str__(self):
        deck_draw = ''
        for card in self.deck:
            deck_draw += '\n' + card.__str__()
            return deck_draw

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        draw_card = self.deck.pop()
        return draw_card


class Hand:
    """
    show cards and keep track of cards used
    """
    def __init__(self):
        self.cards = []
        self.value = 0
        self.ace = 0

    def add_card(self, card):  # add the card to the hand
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.ace += 1

    def ace_transform(self):  # if you are close to 20 the ace equals 1 not 11
        while self.value > 21 and self.ace:
            self.value -= 10
            self.ace -= 1


class Bet:
    """
    keeping track of the wins or bets or the chips I guess
    """

    def __init__(self):
        self.total = 100
        self.bet = 0

    def bet_Win(self):
        self.total += self.bet

    def bet_Lost(self):
        self.total -= self.bet


def hit_or_stand(deck, hand):   # hit or stand
    global playing

    while True:
        ask = input("\nWould you like to hit or stand? Please enter 'h' or 's': ")

        if ask[0].lower() == 'h':
            hit(deck, hand)
        elif ask[0].lower() == 's':
            print("Player stands, Dealer is playing.")
            playing = False
        else:
            print("Sorry! I did not understand that! Please try again!")
            continue
        break

# def test():
#     print(Hand())
#
#
#
#
#
# if __name__ == "__main__":
#     test()



