from array import array

import math

class Vector2d:
    typecode = 'd'

    def __init__(self, x, y):
        self.__x = float(x)
        self.__y = float(y)

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @x.setter
    def x(self, value):
        print("setter of x called")
        self.__x = value

    def __iter__(self):
        return (i for i in (self.x, self.y))

    def __repr__(self):
        class_name = type(self).__name__
        return '{}({!r}, {!r})'.format(class_name, *self)

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return (bytes([ord(self.typecode)]) + bytes(array(self.typecode, self)))

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __abs__(self):
        return math.hypot(self.__x, self.__y)

    def __bool__(self):
        return bool(abs(self))

    def angle(self):
        return math.atan2(self.__y, self.__x)

    def __format__(self, fmt_spec=''):
        if fmt_spec.endswith('p'):
            fmt_spec = fmt_spec[:-1]
            coords = (abs(self), self.angle())
            outer_fmt = '<{}, {}>'
        else:
            coords = self
            outer_fmt = '({}, {})'
        components = (format(c, fmt_spec) for c in coords)
        return outer_fmt.format(*components)

    # inside class Vector2d:
    def __hash__(self):
        return hash(self.x) ^ hash(self.y)


    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(*memv)


v1 = Vector2d(3, 4)

'''
print(v1.x, v1.y)

x, y = v1
print(x, y)

print(v1)

v1_clone = eval(repr(v1))
print(v1 == v1_clone)
print(v1)

octets = bytes(v1)
print(octets)

print(bool(v1), bool(Vector2d(0, 0)))

try:
    print(format(v1, '.3f'))
except Exception as e:
    print(e)

print(format(Vector2d(1, 1), 'p'))
print(format(Vector2d(1, 1), '.3ep'))
print(format(Vector2d(1, 1), '0.5fp'))
'''

'''
v1 = Vector2d(3, 4)
v2 = Vector2d(3.1, 4.2)

try:
    print(hash(v1))
    print(hash(v2))
except Exception as e:
    print(e)

print(set([v1, v2]))
# x,y = v1
# for i in v1:
#     print(i)
print(v1)
'''



v1_clone = Vector2d.frombytes(bytes(v1))
print(v1_clone)
print(v1 == v1_clone)
print(v1_clone.x)
v1_clone.x = 25
print(v1_clone.x)