# -*- coding: utf-8 -*-

from operator import add
from functools import reduce

#==============================================================================
def factorial(n):
    return 1 if n < 2 else n * factorial(n-1)
fact = factorial
#==============================================================================
'''
print(factorial(42))
print(factorial.__doc__)
print(type(factorial))


print(fact(5))
print(list(map(fact, range(11))))
'''
#==============================================================================
'''
def count_it_down(n):
    if n > 1:
        print(n)
        count_it_down(n-1)
    else: print(n)
    
count_it_down(5)
'''
#==============================================================================
'''
A function that takes a function as argument or returns a function as result is 
a higherorder function. 
'''

'''
def reverse(word): 
    return word[::-1]

fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']

print(sorted(fruits, key=len))
print(reverse('testing'))
print(sorted(fruits, key=reverse))

def multiply(x):
    return (x*x)
def add(x):
    return (x+x)

funcs = [multiply, add]
for i in range(5):
    value = tuple(map(lambda x: x(i), funcs))
    print(value)

print(list(map(fact, range(6))))
print([fact(n) for n in range(6)])
print(list(map(factorial, filter(lambda n: n % 2, range(6))))) # for i in range(6): print(i % 2, i)
print([factorial(n) for n in range(6) if n % 2])

old = reduce(add, range(100))
new = sum(range(100))

assert old == new
print(old, new)

product = reduce((lambda x, y: x * y), [1, 2, 3, 4])
'''
#==============================================================================
'''
import random
class BingoCage():
    def __init__(self, items):
        self._items = list(items)
        random.shuffle(self._items)
        self.sequence = []
    def pick(self):
        try:
            pick = self._items.pop()
            self.sequence.append(pick)
        except IndexError:
            raise LookupError('pick from empty BingoCage')
    def __call__(self):
        print('im being called?!')
        return self.pick()

class foo():
    def __init__(self):
        print('hola')
    def __call__(self):
        print('hello?')
        
bar = foo() # or bar = foo; bar()
bar()

bingo = BingoCage(range(10))
bingo.pick()

bingo()
print(callable(bingo))
print(bingo._items)
'''
###############################################################################

"""
Here we use a simple class with a __call__ method to calculate factorials 
(through a callable object) instead of a factorial function that contains 
a static variable (as that's not possible in Python).
"""

class Factorial:
    def __init__(self):
        self.cache = {}
    def __call__(self, n):
        if n not in self.cache:
            if n == 0:
                self.cache[n] = 1
            else:
                self.cache[n] = n * self.__call__(n-1)
        return self.cache[n]

fact = Factorial()

for i in xrange(10):                                                             
    print("{}! = {}".format(i, fact(i)))

print(dir(factorial))

