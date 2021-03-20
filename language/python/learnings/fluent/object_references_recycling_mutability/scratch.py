
'''
a = [1, 2, 3]
b = a
a.append(4)
print(b)

class Gizmo:
    def __init__(self):
        print('Gizmo id: %d' % id(self))
    def __call__(self, a):
        print('called', a)

a = Gizmo()
a('c')

try:
    y = Gizmo() * 10
except Exception as e:
    print(e)
print(dir())
'''

'''
charles = {'name': 'Charles L. Dodgson', 'born': 1832}
lewis = charles
print(lewis is charles)
print(id(charles), id(lewis))
lewis['balance'] = 950
print(charles)

alex = {'name': 'Charles L. Dodgson', 'born': 1832, 'balance': 950}
print(alex == charles)
print(alex is not charles)
'''

'''
t1 = (1, 2, [30, 40])
t2 = (1, 2, [30, 40])

print(t1 == t2)

print(id(t1[-1]))
print(id(t1[-1]))
print(t1[-1])

t1[-1].append(99)
print(t1)

print(id(t1[-1]))
print(t1 == t2)
'''

'''
l1 = [3, [55, 44], (7, 8, 9)]
l2 = list(l1)

print(l2 == l1)
print(l2 is l1)
'''

'''
l1 = [3, [66, 55, 44], (7, 8, 9)]
l2 = list(l1) #

print(l1)

l1.append(100) #
l1[1].remove(55) #

print('l1:', l1)
print('l2:', l2)

l2[1] += [33, 22] #
l2[2] += (10, 11) #

print('l1:', l1)
print('l2:', l2)
'''

'''
class Bus:

    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = list(passengers)

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)

import copy

bus1 = Bus(['Alice', 'Bill', 'Claire', 'David'])
bus2 = copy.copy(bus1)
bus3 = copy.deepcopy(bus1)

print(id(bus1), id(bus2), id(bus3))

bus1.drop('Bill')

print(bus2.passengers)

print(id(bus1.passengers), id(bus2.passengers), id(bus3.passengers))

print(bus3.passengers)


from copy import deepcopy

a = [10, 20]
b = [a, 30]

a.append(b)
print(a)

c = deepcopy(a)
print(c)

'''

'''
def f(a, b):
    a += b
    return a

x = 1
y = 2

print(f(x, y))
print(x, y)

a = [1, 2]
b = [3, 4]

print(f(a, b))
print(a, b) # a changed

t = (10, 20)
u = (30, 40)

print(f(t, u))
print(t, u) # tuple didn't change
'''

class HauntedBus:

    """A bus model haunted by ghost passengers"""

    def __init__(self, passengers=[]):
        self.passengers = passengers

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)

bus1 = HauntedBus(['Alice', 'Bill'])

print(bus1.passengers)
print(HauntedBus.__init__.__defaults__)

bus1.pick('Charlie')
bus1.drop('Alice')

print(bus1.passengers)

bus2 = HauntedBus()
bus2.pick('Carrie')

print(HauntedBus.__init__.__defaults__)
print(bus2.passengers)

bus3 = HauntedBus()

print(bus3.passengers)

bus3.pick('Dave')

print(bus2.passengers)
print(bus2.passengers is bus3.passengers)
print(bus1.passengers)

# The problem is that Bus instances that don’t get an initial passenger list end up sharing
# the same passenger list among themselves

print(dir(HauntedBus.__init__))
print(HauntedBus.__init__.__defaults__)

# Verify that bus2.passengers is an alias bound to the first element of the
# HauntedBus.__init__.__defaults__ attribute:
print(HauntedBus.__init__.__defaults__[0] is bus2.passengers)

# more reading & examples: http://docs.python-guide.org/en/latest/writing/gotchas/