import operator
import reprlib
import math
import numbers
import functools
import itertools

from array import array
from itertools import zip_longest

# print(2 * 3 * 4 * 5) # the result we want: 5! == 120
# print(functools.reduce(lambda a,b: a*b, range(1, 6)))
#
# n = 0
# for i in range(1, 6):
#     n ^= i
#
# print(n)
#
# functools.reduce(lambda a, b: a^b, range(6))
# functools.reduce(operator.xor, range(6))


class Vector:

    typecode = 'd'

    def __init__(self, components):
        self._components = array(self.typecode, components)

    def __iter__(self):
        return iter(self._components)

    def __repr__(self):
        components = reprlib.repr(self._components)
        components = components[components.find('['):-1]
        return 'Vector({})'.format(components)

    def __str__(self):
        print('1')
        return str(tuple(self))

    def __bytes__(self):
        return (bytes([ord(self.typecode)]) +
                bytes(self._components))

    '''
    def __eq__(self, other):
        return tuple(self) == tuple(other)
        
        
    def __eq__(self, other):
        return len(self) == len(other) and all(a == b for a, b in zip(self, other))
    '''

    def __eq__(self, other):
        if len(self) != len(other):  #
            return False

        for a, b in zip(self, other):  #
            if a != b:  #
                return False
        return True  #

    def __abs__(self):
        return math.sqrt(sum(x * x for x in self))

    def __bool__(self):
        return bool(abs(self))

    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(memv)

    '''
    def __len__(self):
        return len(self._components)

    def __getitem__(self, index):
        return self._components[index]
    '''

    def __len__(self):
        return len(self._components)

    def __getitem__(self, index):
        cls = type(self)
        if isinstance(index, slice):
            return cls(self._components[index])
        elif isinstance(index, numbers.Integral):
            return self._components[index]
        else:
            msg = '{cls.__name__} indices must be integers'
            raise TypeError(msg.format(cls=cls))

    shortcut_names = 'xyzt'

    def __getattr__(self, name):
        cls = type(self)
        if len(name) == 1:
            pos = cls.shortcut_names.find(name)
            # pos = self.shortcut_names.find(name) # this works as well
            if 0 <= pos < len(self._components):
                return self._components[pos]
        msg = '{.__name__!r} object has no attribute {!r}'
        raise AttributeError(msg.format(cls, name))

    def __setattr__(self, name, value):
        cls = type(self)

        if len(name) == 1:
            print('here')
            if name in cls.shortcut_names:
                error = 'readonly attribute {attr_name!r}'
            elif name.islower():
                error = "can't set attributes 'a' to 'z' in {cls_name!r}"
            else:
                error = ''
            if error:
                msg = error.format(cls_name=cls.__name__, attr_name=name)
                raise AttributeError(msg)
        super().__setattr__(name, value)

    def __hash__(self):
        hashes = (hash(x) for x in self._components)
        print(self._components, hashes)
        return functools.reduce(operator.xor, hashes, 0)

    def angle(self, n):
        r = math.sqrt(sum(x * x for x in self[n:]))
        a = math.atan2(r, self[n - 1])
        if (n == len(self) - 1) and (self[-1] < 0):
            return math.pi * 2 - a
        else:
            return a

    def angles(self):
        return (self.angle(n) for n in range(1, len(self)))

    def __format__(self, fmt_spec=''):
        if fmt_spec.endswith('h'):  # hyperspherical coordinates
            fmt_spec = fmt_spec[:-1]
            coords = itertools.chain([abs(self)],self.angles())
            outer_fmt = '<{}>'
        else:
            coords = self
            outer_fmt = '({})'

        components = (format(c, fmt_spec) for c in coords)
        return outer_fmt.format(', '.join(components))


# v = Vector(range(5))
# print(v.x)
# print(2 * 3 * 4 * 5)
# print(functools.reduce(lambda a,b: a*b, range(1, 6)))
# print('here')
# print(hash(v))

a = Vector(range(4))
b = Vector(range(4))
print(a)

if a == b: print('yes')
else: print('no')

print(list(zip(range(3), 'ABC')))
print(list(zip(range(3), 'ABC', [0.0, 1.1, 2.2, 3.3])))
print(list(zip_longest(range(3), 'ABCDEF', [0.0, 1.1, 2.2, 3.3], fillvalue=-1)))