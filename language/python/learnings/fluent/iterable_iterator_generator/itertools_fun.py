
import itertools
import operator

gen = itertools.count(1, .5)

print(next(gen))
print(next(gen))
print(next(gen))

# list(itertools.count())  # will make your machine unhappy :(

sample = [5, 4, 2, 8, 7, 6, 3, 0, 9, 1]

print(list(itertools.accumulate(sample)))
print(list(itertools.accumulate(sample, min)))
print(list(itertools.accumulate(sample, max)))

print(list(itertools.accumulate(sample, operator.mul)))
print(list(itertools.accumulate(range(1, 11), operator.mul)))

print(list(enumerate('albatroz', 1)))
print(list(map(operator.mul, range(11), range(11))))
print(list(map(operator.mul, range(11), [2, 4, 8])))

sample = [5, 4, 2, 8, 7, 6, 3, 0, 9, 1]
print((itertools.starmap(lambda a, b: b/a, enumerate(itertools.accumulate(sample), 1))))

print(list(enumerate('123', 2)))

list(itertools.chain('ABC', range(2))) #
# ['A', 'B', 'C', 0, 1]

list(itertools.chain(enumerate('ABC'))) #
# [(0, 'A'), (1, 'B'), (2, 'C')]

list(itertools.chain.from_iterable(enumerate('ABC'))) #
# [0, 'A', 1, 'B', 2, 'C']

list(zip('ABC', range(5))) #
# [('A', 0), ('B', 1), ('C', 2)]

list(zip('ABC', range(5), [10, 20, 30, 40])) #
# [('A', 0, 10), ('B', 1, 20), ('C', 2, 30)]

list(itertools.zip_longest('ABC', range(5))) #
# [('A', 0), ('B', 1), ('C', 2), (None, 3), (None, 4)]

list(itertools.zip_longest('ABC', range(5), fillvalue='?')) #
# [('A', 0), ('B', 1), ('C', 2), ('?', 3), ('?', 4)]

list(itertools.product('ABC', range(2))) # cartesian product
# [('A', 0), ('A', 1), ('B', 0), ('B', 1), ('C', 0), ('C', 1)]

suits = 'spades hearts diamonds clubs'.split()
list(itertools.product('AK', suits))
# [('A', 'spades'), ('A', 'hearts'), ('A', 'diamonds'), ('A', 'clubs'),
#  ('K', 'spades'), ('K', 'hearts'), ('K', 'diamonds'), ('K', 'clubs')]

list(itertools.product('ABC'))
# [('A',), ('B',), ('C',)]

list(itertools.product('ABCD', repeat=2))
# [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'B'),
#  ('B', 'C'), ('C', 'A'), ('C', 'B'), ('C', 'C')]

list(itertools.product(range(2), repeat=3))
# [(0, 0, 0), (0, 0, 1), (0, 1, 0), (0, 1, 1), (1, 0, 0),
#  (1, 0, 1), (1, 1, 0), (1, 1, 1)]

# Example 14-19. count and repeat

ct = itertools.count()
next(ct)
# 0

next(ct), next(ct), next(ct)
# (1, 2, 3)

list(itertools.islice(itertools.count(1, .3), 3))
# [1, 1.3, 1.6]

cy = itertools.cycle('ABC')

next(cy)
# 'A'

list(itertools.islice(cy, 7))
# ['B', 'C', 'A', 'B', 'C', 'A', 'B']

rp = itertools.repeat(7)

next(rp), next(rp)
# (7, 7)

list(itertools.repeat(8, 4))
# [8, 8, 8, 8]

list(map(operator.mul, range(11), itertools.repeat(5)))
# [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50]

list(itertools.combinations('ABC', 2))
# [('A', 'B'), ('A', 'C'), ('B', 'C')]

list(itertools.combinations_with_replacement('ABC', 2)) #
# [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'B'), ('B', 'C'), ('C', 'C')]

list(itertools.permutations('ABC', 2)) #
# [('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')]

list(itertools.product('ABC', repeat=2)) #
# [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'B'), ('B', 'C'), ('C', 'A'), ('C', 'B'), ('C', 'C')]


for char, group in itertools.groupby('LLLLAAAGG'):
    print(char, '->', list(group))

animals = ['duck', 'eagle', 'rat', 'giraffe', 'bear',
           'bat', 'dolphin', 'shark', 'lion']
animals.sort(key=len) #
print(animals)
# ['rat', 'bat', 'duck', 'bear', 'lion', 'eagle', 'shark', 'giraffe', 'dolphin']

for length, group in itertools.groupby(animals, len): #
    print(length, '->', list(group))
# 3 -> ['rat', 'bat']
# 4 -> ['duck', 'bear', 'lion']
# 5 -> ['eagle', 'shark']
# 7 -> ['giraffe', 'dolphin']

for length, group in itertools.groupby(reversed(animals), len):
    print(length, '->', list(group))
# -> ['dolphin', 'giraffe']
# -> ['shark', 'eagle']
# -> ['lion', 'bear', 'duck']
# -> ['bat', 'rat']

'''
>>> list(itertools.tee('ABC'))
[<itertools._tee object at 0x10222abc8>, <itertools._tee object at 0x10222ac08>]
>>> g1, g2 = itertools.tee('ABC')
>>> next(g1)
'A'
>>> next(g2)
'A'
>>> next(g2)
'B'
>>> list(g1)
['B', 'C']
>>> list(g2)
['C']
>>> list(zip(*itertools.tee('ABC')))
[('A', 'A'), ('B', 'B'), ('C', 'C')]
<<<<<<< HEAD
'''
