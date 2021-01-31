from collections import namedtuple

Subscriber = namedtuple('Subscriber', ['addr', 'joined'])

sub = Subscriber('jonesy@example.com', '2012-10-19')

print(sub.addr, sub.joined)
print(sub)

addr, joined = sub  # nothing like some unpacking!
print(addr, joined)

#  ================================================================

Stock = namedtuple('Stock', ['name', 'shares', 'price'])


def compute_cost1(records):
    total = 0.0
    for rec in records:
        s = Stock(*rec)
        total += s.shares * s.price
    return total


# as opposed to this setup


def compute_cost2(records):
    total = 0.0
    for rec in records:
        total += rec[1] * rec[2]
    return total


s = Stock('ACME', 100, 123.45)
print(Stock(name='ACME', shares=100, price=123.45))

try:
    s.shares = 75
except AttributeError:
    print('cant swap values like that')
finally:
    s = s._replace(shares=75)
print(s)

#  ================================================================


Stock = namedtuple('Stock', ['name', 'shares', 'price', 'date', 'time'])

# Create a prototype instance
stock_prototype = Stock('', 0, 0.0, None, None)


# Function to convert a dictionary to a Stock
def dict_to_stock(s):
    return stock_prototype._replace(**s)


a = {'name': 'ACME', 'shares': 100, 'price': 123.45}
a = dict_to_stock(a)
print(a)

b = {'name': 'ACME', 'shares': 100, 'price': 123.45, 'date': '12/17/2012'}
b = dict_to_stock(b)
print(b)

#  ================================================================