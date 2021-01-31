
'''
As we´ve seen, Python calls iter(x) when it needs to iterate over an object x.
But iter has another trick: it can be called with two arguments to create an iterator
from a regular function or any callable object. In this usage, the first argument must be
a callable to be invoked repeatedly (with no arguments) to yield values, and the second
argument is a sentinel: a marker value which, when returned by the callable, causes the
iterator to raise StopIteration instead of yielding the sentinel.

The following example shows how to use iter to roll a 6-sided die until a 1 is rolled:
'''

import random


def d6():
    ri = random.randint(1, 6)
    print(str(ri) + '===')
    return ri

print('here')
d6_iter = iter(d6, 1)
print(list(d6_iter))
print('here1')

for roll in d6_iter:
    print(roll)
    print('rolled')


print('here2')
d6_iter = iter(d6, 1)
print('here3')

for roll in d6_iter:
    print(roll)
    print('rolled')