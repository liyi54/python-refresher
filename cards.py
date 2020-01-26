import random

class Card:
    suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
    ranks = ["narf", "Ace", "2", "3", "4", "5", "6", "7",
             "8", "9", "10", "Jack", "Queen", "King"]

    def __init__(self, suit=0, rank=0):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return "{0} of {1}".format(self.ranks[self.rank], self.suits[self.suit])

    def cmp(self, other):
        if self.suit < other.suit:
            return -1
        elif self.suit > other.suit:
            return 1
        elif self.rank < other.rank:
            return -1
        elif self.rank > other.rank:
            return 1
        else:
            return 0

    def __lt__(self, other):
        return self.cmp(other) < 0

    def __le__(self, other):
        return self.cmp(other) <= 1

    def __gt__(self, other):
        return self.cmp(other) > 0

    def __ge__(self, other):
        return self.cmp(other) >= 0

    def __ne__(self, other):
        return self.cmp(other) != 0

    def __eq__(self, other):
        return self.cmp(other) == 0


class Deck:
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1,14):
                self.cards.append(Card(suit,rank))

    def __str__(self):
        s = ""
        for i in range(len(self.cards)):
            s += " " * i + str(self.cards[i]) + "\n"  # We multiple by i to cascade the cards
        return s

    def shuffle1(self):
        rng = random.Random()
        for i in range(len(self.cards)):
            j = rng.randrange(i, len(self.cards))
            (self.cards[i], self.cards[j]) = (self.cards[j], self.cards[i])

    def shuffle2(self):
        rng = random.Random()
        rng.shuffle(self.cards)

    def remove(self, card):
        if card in self.cards:
            self.cards.remove(card)
            return True
        else:
            return False

    def pop(self):
        return self.cards.pop()

    def isEmpty(self):
        return len(self.cards) == 0

# Card1 = Card(0, 3)
# Card2 = Card(1, 11)
# Card3 = Card(0, 3)
#
# print(Card1 > Card2)
# print(Card1 == Card3)

red_deck = Deck()
blue_deck = Deck()

print(red_deck)