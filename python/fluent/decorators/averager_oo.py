'''
def foo():
    print('wsup')

bar = foo
bar() # wsup
'''

'''
def make_multiplier_of(n):
    def multiplier(x):
        return x * n
    return multiplier

# Multiplier of 3
times3 = make_multiplier_of(3)

# Multiplier of 5
times5 = make_multiplier_of(5)

# Output: 27
print(times3(9))

# Output: 15
print(times5(3))

# Output: 30
print(times5(times3(2)))
'''



class Averager:
    def __init__(self):
        self.series = []
    def __call__(self, new_value):
        self.series.append(new_value)
        total = sum(self.series)
        return total / len(self.series)

avg = Averager()

print(avg(10))
print(avg(11))
print(avg(12))


def make_averager():
    series = []
    def averager(new_value):
        series.append(new_value)
        total = sum(series)
        return total/len(series)
    return averager


avg = make_averager()

print(avg(10))
print(avg(11))
print(avg(12))

print(avg.__code__.co_varnames)
print(avg.__code__.co_freevars)


# =======================================
# The nonlocal declaration
# =======================================

x = 25


def make_averager():

    count = 0
    total = 0

    def averager(new_value):
        print(x*2)
        nonlocal count, total
        count += 1 # this is would be an issue w/o nonlocal
        total += new_value # this would be an issue w/o nonlocal
        return total / count

    return averager


avg = make_averager()
print(avg(10))