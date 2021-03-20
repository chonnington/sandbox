import math
from itertools import compress

# ==============================================================================

mylist = [1, 4, -5, 10, -7, 2, 3, -1]
print([n for n in mylist if n > 0])

pos = (n for n in mylist if n > 0)
print(type(pos))

for x in pos:
    print(x)

# ==============================================================================

values = ['1', '2', '-3', '-', '4', 'N/A', '5']


def is_int(val):
    try:
        x = int(val)
        return True
    except ValueError:
        return False


ivals = list(filter(is_int, values))
print(ivals)

mylist = [1, 4, -5, 10, -7, 2, 3, -1]
print([math.sqrt(n) for n in mylist if n > 0])

clip_neg = [n if n > 0 else 0 for n in mylist]
print(clip_neg)

clip_pos = [n if n < 0 else 0 for n in mylist]
print(clip_pos)

# ==============================================================================

addresses = ['5412 N CLARK',       # 0
             '5148 N CLARK',       # 1
             '5800 E 58TH',        # 2
             '2122 N CLARK',       # 3
             '5645 N RAVENSWOOD',  # 4
             '1060 W ADDISON',     # 5
             '4801 N BROADWAY',    # 6
             '1039 W GRANVILLE']   # 7

counts = [0, 3, 10, 4, 1, 7, 6, 1]

more5 = [n > 5 for n in counts]
print(more5)

print(list(compress(addresses, more5)))