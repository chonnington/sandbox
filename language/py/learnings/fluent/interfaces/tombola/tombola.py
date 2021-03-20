import abc

# BaseException
# ├── SystemExit
# ├── KeyboardInterrupt
# └── Exception
# ├── StopIteration
# ├── ArithmeticError
# │ ├── FloatingPointError
# │ ├── OverflowError
# │ └── ZeroDivisionError
# ├── AssertionError
# ├── AttributeError
# ├── BufferError
# ├── EOFError
# ├── ImportError
# ├── LookupError
# │ ├── IndexError
# │ └── KeyError
# ├── MemoryError


class Tombola(abc.ABC):  # To define an ABC, subclass abc.ABC

    @abc.abstractmethod
    def load(self, iterable):
        """Add items from an iterable."""

    @abc.abstractmethod
    def pick(self):
        """Remove item at random, returning it.
        This method should raise `LookupError` when the instance is empty.
        """

    def loaded(self):
        """Return `True` if there's at least 1 item, `False` otherwise."""
        return bool(self.inspect())

    def inspect(self):
        """Return a sorted tuple with the items currently inside."""
        items = []
        while True:
            try:
                items.append(self.pick())
            except LookupError:
                break
        self.load(items)
        return tuple(sorted(items))


# class Fake(Tombola):
#     def pick(self):
#         return 13
# Fake
# f = Fake()  # this will error out; all required abstract methods have not been implemented


# class BingoCage(Tombola):
#
#     def __init__(self, items):
#         self._randomizer = random.SystemRandom()
#         self._items = []
#         self.load(items)
#
#     def load(self, items):
#         self._items.extend(items)
#         self._randomizer.shuffle(self._items)
#
#     def pick(self):
#         try:
#             return self._items.pop()
#         except IndexError:
#             raise LookupError('pick from empty BingoCage')
#
#     def __call__(self):
#         self.pick()


# class LotteryBlower(Tombola):
#
#     def __init__(self, iterable):
#         self._balls = list(iterable)
#
#     def load(self, iterable):
#         self._balls.extend(iterable)
#
#     def pick(self):
#         try:
#             position = random.randrange(len(self._balls))
#         except ValueError:
#             raise LookupError('pick from empty BingoCage')
#         return self._balls.pop(position)
#
#     def loaded(self):
#         return bool(self._balls)
#
#     def inspect(self):
#         return tuple(sorted(self._balls))


# a = []
# print(bool(a))
# a.append(1)
# print(bool(a))


# from random import randrange
#
#
# @Tombola.register
# class TomboList(list):  # Tombolist extends list.
#
#     def pick(self):
#         if self:
#             position = randrange(len(self))
#             return self.pop(position)
#         else:
#             raise LookupError('pop from empty TomboList')
#
#     load = list.extend  # Tombolist.load is the same as list.extend
#
#     def loaded(self):
#         return bool(self)
#
#     def inspect(self):
#         return tuple(sorted(self))


# print(issubclass(TomboList, Tombola))
# t = TomboList(range(100))
# print(isinstance(t, Tombola))

# a = range(25)
# print(type(a))


'''
Tombola is not in Tombolist.__mro__, so 
Tombolist does not inherit any methods from Tombola.
'''

# print(TomboList.__mro__)