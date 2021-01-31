


class A:
    def ping(self):
        print('ping:', self)


class B(A):
    def pong(self):
        print('pong:', self)


class C(A):
    def pong(self):
        print('PONG:', self)


class D(B, C):  # The left side first

    def ping(self):
        super().ping()  # A.ping(self)
        print('post-ping:', self)
        a = str(self)

    def pingpong(self):
        self.ping()
        super().ping()
        self.pong()
        super().pong()
        C.pong(self)


d = D()

# d.pong()
# print(D.__mro__)
# d.ping() #

d.pingpong()


def print_mro(cls):
    print()
    print(cls, ', '.join(c.__name__ for c in cls.__mro__))


print(bool.__mro__)

from frenchdeck2 import FrenchDeck2
print(print_mro(FrenchDeck2))

import numbers
print_mro(numbers.Integral)

import io
print_mro(io.BytesIO)
print_mro(io.TextIOWrapper)

import tkinter
print_mro(tkinter.Text)