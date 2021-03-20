import collections


class Foo:

    def __init__(self, x, y):
        self.__x1 = float(x)
        self.__y = float(y)

    @property
    def x1(self):
        return self.__x1

    @property
    def y(self):
        return self.__y


a = Foo(1, 2)
print(a.x1)
del a, Foo


# Example 11-3. Partial sequence protocol implementation with __getitem__: enough
# for item access, iteration and the in operator.
class Foo:
    def __getitem__(self, pos):
        return range(0, 30, 10)[pos]


f = Foo()
# print(f[1])
#
# for i in f:
#     print(i)
#
# print(20 in f, 15 in f)

#  ==============================================================================================

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:

    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                      for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        # print('getting invoked!')
        return self._cards[position]


cards = FrenchDeck()

# print(cards[0])

deck_length = len(cards)

# for card in cards.cards:
#     print(card)

from random import shuffle

# l = list(range(10))
# print(l)
# shuffle(l)
# print(l)


deck = FrenchDeck()

# shuffle(deck)
# try:
#     shuffle(deck)
# except TypeError as e:
#     print(e)


# def set_card(deck, position, card):
#     deck._cards[position] = card
#
# print(deck[:3])
#
# try:
#     shuffle(deck)
# except TypeError:
#     try:
#         print(deck.__setitem__)
#     except Exception as e:
#         print(e)
#         FrenchDeck.__setitem__ = set_card
# finally:
#     shuffle(deck)
#
# print(deck[:3])

'''

>>> def set_card(deck, position, card):
... deck._cards[position] = card
...

>>> FrenchDeck.__setitem__ = set_card
>>> shuffle(deck)
>>> deck[:5]

[Card(rank='3', suit='hearts'), Card(rank='4', suit='diamonds'), Card(rank='4',
suit='clubs'), Card(rank='7', suit='hearts'), Card(rank='9', suit='spades')]

create a function that takes deck, position and card as arguments.
assign that function to an attribute named __setitem__ in the FrenchDeck class.
deck can now be sorted because FrenchDeck now implements the necessary
method of the mutable sequence protocol.

The signature of the __setitem__ special method is defined in the Emulating container
types section of the Data model chapter of the Python Language Reference. Here we
named the arguments deck, position, card — and not self, key, value as in the
Language Reference — to show that every Python method starts life as a plain function,
and naming the first argument self is merely a convention. This is OK in a console
session, but in a Python source file it’s much better to use self, key and value as documented.


'''


class Struggle:
    def __len__(self): return 23

from collections import abc

print(isinstance(Struggle(), abc.Sized))

field_names = None

try:
    field_names = field_names.replace(',', ' ').split()
except AttributeError:
    pass
field_names = tuple(field_names)