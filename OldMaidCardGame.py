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

    def is_empty(self):
        return len(self.cards) == 0

    def deal(self, hands, num_cards=999):  # The num_cards default value is all the cards
        num_hands = len(hands)
        for i in range(num_cards):
            if self.is_empty():
                break
            card = self.pop()
            hand = hands[i % num_hands]  # This distributes the cards using a round-robin approach
            hand.add(card)


class Hand(Deck):
    def __init__(self, name=""):
        self.cards = []
        self.name = name

    def add(self, card):
        self.cards.append(card)

    def __str__(self):  # This overrides the string method in the Deck class
        s = "Hand " + self.name
        if self.is_empty():
            s += " is empty \n"
        else:
            s += " contains: \n"
        return s + Deck.__str__(self)

    # def print_hands(self, names):
    #     hands = ""
    #     for name in names:
    #         s = "Hand " + self.name
    #         if self.is_empty():
    #             s += " is empty \n"
    #         else:
    #             s += " contains: \n"
    #         hands += s + Deck.__str__(self)
    #     return hands



class CardGame:
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle2()


class OldMaidHand(Hand):
    def remove_matches(self):
        count = 0
        original_cards = self.cards.copy()
        for card in original_cards:
            match = Card(3 - card.suit, card.rank)  # Using cards of the same rank and color to match the cards
            if match in self.cards:
                self.cards.remove(card)
                self.cards.remove(match)
                print("Hand {0}: {1} matches card {2}".format(self.name, card, match))
                count += 1
        return count


class OldMaidGame(CardGame):

    def find_neighbor(self, i):
        num_hands = len(self.hands)
        for next in range(1, num_hands):
            neighbor = (i + next) % num_hands
            if not self.hands[neighbor].is_empty():
                return neighbor

    def play_one_turn(self, i):
        if self.hands[i].is_empty():
            return 0
        neighbor = self.find_neighbor(i)
        picked_card = self.hands[neighbor].pop()
        self.hands[i].add(picked_card)
        print("Hand {0} picked {1}".format(self.hands[i].name, picked_card))
        count = self.hands[i].remove_matches()
        self.hands[i].shuffle2()
        return count

    def remove_all_matches(self):
        count = 0
        for hand in self.hands:
            count += hand.remove_matches()
        return count

    def print_hands(self):
        for hand in self.hands:
            print(hand.__str__())

    def play(self, names):
        # We remove the queen of clubs
        self.deck.remove(Card(0,12))

        # Make a hand for each player
        self.hands = []
        for name in names:
            self.hands.append(OldMaidHand(name))
        print("---- Hands made for each player ----")

        # Deal the cards
        self.deck.deal(self.hands)
        print("---- Cards have been dealt ----")

        # Remove initial matches
        # for name in names:
        #     matches = OldMaidHand(name).remove_matches()
        matches = self.remove_all_matches()
        print("--- Matches discarded, play begins ---")
        self.print_hands()

        # Play until all 50 cards are matched: because the queen of clubs can't be matched
        turn = 0
        num_hands = len(self.hands)
        while matches < 25:
            matches += self.play_one_turn(turn)
            turn = (turn + 1) % num_hands
        print("--- Game Over ---")
        self.print_hands()





# Card1 = Card(0, 3)
# Card2 = Card(1, 11)
# Card3 = Card(0, 3)
#
# print(Card1 > Card2)
# print(Card1 == Card3)

# red_deck = Deck()
# blue_deck = Deck()
#
# print(red_deck)

# deck = Deck()
# deck.shuffle2()
#
# hand1 = Hand("frank") # Each hand is an object
# hand2 = Hand("swiss")
# # print(hand.cards)
# deck.deal([hand1, hand2], 5) # We pass a list of objects representing a list of hands
#
# # print(len([hand]))
# print(hand1)
# print(hand2)

game = OldMaidGame()
game.play(['Frank', 'John', 'Jeff', 'Derrick', 'Joe'])

# print(hand)

# print(hand.remove_matches())
