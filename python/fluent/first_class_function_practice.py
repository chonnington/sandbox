# -*- coding: utf-8 -*-
#==============================================================================
'''
from operator import add
from functools import reduce

def factorial(n):
    return 1 if n < 2 else n * factorial(n-1)
fact = factorial
'''
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

'''
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

for i in range(10):                                                             
    print("{}! = {}".format(i, fact(i)))

print(dir(factorial))

class C: pass #
obj = C() #
def func(): pass #
sorted(set(dir(func)) - set(dir(obj))) #
'''
###############################################################################
'''
#def foo(*positional, **keywords):
#    print("Positional:", positional)
#    print("Keywords:", keywords)
#    for pos in positional: print(pos)
#print(foo('one','two',c='three',d='four'))

def tag(name, *content, cls=None, **attrs):
    """Generate one or more HTML tags"""
    if cls is not None:
        print(1)
        attrs['class'] = cls
        attrs['mah'] = 'fa'
    if attrs:
        print(2)
        attr_str = ''.join(' %s="%s"' % (attr, value) for attr, value in sorted(attrs.items()))
    else:
        print(3)
        attr_str = ''
    if content:
        print(4)
        return '\n'.join('<%s%s>%s</%s>' % (name, attr_str, c, name) for c in content)
    else:
        print(5)
        return '<%s%s />' % (name, attr_str)

print(tag('br'))

print(tag('p', 'hello'))

print(tag('p', 'hello', 'world'))

print(tag('p', 'hello', id=33, foo='bar'))

print(tag('p', 'hello', 'world', id=33, cls='slc', foo='bar'))

print(tag('p', 'hello', 'world', cls='sidebar'))

print(tag(content='testing', name="img"))

my_tag = {'name': 'img',
          'title': 'Sunset Boulevard',
          'src': 'sunset.jpg', 
          'cls': 'framed'}

print(tag(**my_tag))

def f(a, *, b): return a, b
print(f(1, b=2))
'''
###############################################################################

'''
import bobo
@bobo.query('/')
def hello(person): return 'Hello %s!' % person
'''

'''
def clip(text, max_len=80):
    """
    Return text clipped at the last space before or after max_len
    """
    end = None
    if len(text) > max_len:
        space_before = text.rfind(' ', 0, max_len)
        if space_before >= 0:
            end = space_before
        else:
            space_after = text.rfind(' ', max_len)
    if space_after >= 0:
        end = space_after
    if end is None: # no spaces were found
        end = len(text)
    return text[:end].rstrip()
'''
'''
from clip import clip

print(clip.__defaults__)
print(clip.__code__) 
print(clip.__code__.co_varnames)
print(clip.__code__.co_argcount)

from clip import clip
from inspect import signature
sig = signature(clip)

print(str(sig))
for name, param in sig.parameters.items():
    print(param.kind, ':', name, '=', param.default)
'''
#==============================================================================
'''
import inspect

sig = inspect.signature(tag)
my_tag = {'name': 'img',
          'title': 'Sunset Boulevard',
          'src': 'sunset.jpg', 
          'cls': 'framed'}

bound_args = sig.bind(**my_tag)
print(); print(bound_args)

del my_tag['name']

try:
    bound_args = sig.bind(**my_tag)
except Exception as e:
    print(); print(e)
'''
#==============================================================================
'''
from clip_annot import clip
print(clip.__annotations__)
'''
#==============================================================================
'''
from functools import reduce

def fact1(n):
    return reduce(lambda a, b: a*b, range(1, n+1))
    
print(fact1(5))

from functools import reduce
from operator import mul

def fact2(n):
    return reduce(mul, range(1, n+1))

print(fact2(5))
'''
#==============================================================================
'''
metro_data = [
('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]

from operator import itemgetter
for city in sorted(metro_data, key=itemgetter(2), reverse=False):
    print(city)

cc_name = itemgetter(1, 0, 3)
for city in metro_data:
    print(cc_name(city))
'''
#==============================================================================
'''
from collections import namedtuple

metro_data = [
('Tokyo', 'JP', 36.933, (35.689722, 139.691667, 1)),
('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889, 2)),
('Mexico City', 'MX', 20.142, (19.433333, -99.133333, 3)),
('New York-Newark', 'US', 20.104, (40.808611, -74.020386, 4)),
('Sao Paulo', 'BR', 19.649, (-23.547778, -46.635833, 5)),
]

LatLong = namedtuple('LatLong', 'lat long rank') #

Metropolis = namedtuple('Metropolis', 'name cc pop coord') #

metro_areas = [Metropolis(name, cc, pop, LatLong(lat, long, rank)) 
    for name, cc, pop, (lat, long, rank) in metro_data]

#for i in metro_areas: print(i)

print(metro_areas[0])
print(metro_areas[0].coord.lat)

from operator import attrgetter

name_lat = attrgetter('name', 'coord.lat') #
for city in sorted(metro_areas, key=attrgetter('coord.lat')):
    print(name_lat(city))
    
import operator
print([name for name in dir(operator) if not name.startswith('_')])
'''
#==============================================================================
'''
from operator import methodcaller
s = 'The time has come'
upcase = methodcaller('upper')
upcase(s)

hiphenate = methodcaller('replace', ' ', '-')
hiphenate(s)

print(str.upper(s))
'''
#==============================================================================

from operator import mul
from functools import partial

import unicodedata, functools

triple = partial(mul, 3)

print(triple(7))
print(triple(triple(7)))
print(list(map(triple, range(1, 10))))

nfc = partial(unicodedata.normalize, 'NFC')
s1 = 'café'
s2 = 'cafe\u0301'

print(s1, s2)
print(s1 == s2)
print(nfc(s1) == nfc(s2))

def tag(name, *content, cls=None, **attrs):
    """Generate one or more HTML tags"""
    if cls is not None:
        print(1)
        attrs['class'] = cls
        attrs['mah'] = 'fa'
    if attrs:
        print(2)
        attr_str = ''.join(' %s="%s"' % (attr, value) for attr, value in sorted(attrs.items()))
    else:
        print(3)
        attr_str = ''
    if content:
        print(4)
        return '\n'.join('<%s%s>%s</%s>' % (name, attr_str, c, name) for c in content)
    else:
        print(5)
        return '<%s%s />' % (name, attr_str)
    
picture = partial(tag, 'img', 'world', do = 'fuh', cls='pic-frame')

print(picture(src='wumpus.jpeg'))
print(picture)
print(picture.func)
print(picture.args)
print(picture.keywords)




