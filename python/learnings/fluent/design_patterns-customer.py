# =======================================================
# Object Strategy
# =======================================================

from abc import ABC, abstractmethod
from collections import namedtuple

Customer = namedtuple('Customer', 'name fidelity')


class LineItem:
    
    def __init__(self, product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = price
        
    def total(self):
        return self.price * self.quantity


class Order:  # the Context

    def __init__(self, customer, cart, promotion=None):
        self.customer = customer
        self.cart = list(cart)
        self.promotion = promotion
        self.foo = 'bar'
        
    def total(self):
        if not hasattr(self, '__total'):
            self.__total = sum(item.total() for item in self.cart)
        return self.__total
    
    def due(self):
        if self.promotion is None:
            discount = 0
        else:
            discount = self.promotion.discount(self)
        return self.total() - discount
           
    def __repr__(self):
        fmt = '<Order total: {:.2f} due: {:.2f}>'
        return fmt.format(self.total(), self.due())
    
    
class Promotion(ABC):  # the Strategy: an Abstract Base Class
    @abstractmethod
    def discount(self, order):
        """Return discount as a positive dollar amount"""


class FidelityPromo(Promotion):  # first Concrete Strategy
    """5% discount for customers with 1000 or more fidelity points"""
    def discount(self, order):
        return order.total() * .05 if order.customer.fidelity >= 1000 else 0


class BulkItemPromo(Promotion):  # second Concrete Strategy
    """10% discount for each LineItem with 20 or more units"""
    def discount(self, order):
        discount = 0
        for item in order.cart:
            if item.quantity >= 20:
                discount += item.total() * .1
        return discount


class LargeOrderPromo(Promotion):  # third Concrete Strategy
    """7% discount for orders with 10 or more distinct items"""
    def discount(self, order):
        distinct_items = {item.product for item in order.cart}
        if len(distinct_items) >= 10:
            return order.total() * .07
        return 0


joe = Customer('John Doe', 0)
ann = Customer('Ann Smith', 1100)

cart = [LineItem('banana', 4, .5),
        LineItem('apple', 10, 1.5),
        LineItem('watermellon', 5, 5.0)]

print(Order(joe, cart, FidelityPromo()))
print(Order(ann, cart, FidelityPromo()))

banana_cart = [LineItem('banana', 30, .5),
               LineItem('apple', 10, 1.5)]

print(Order(joe, banana_cart, BulkItemPromo()))

long_order = [LineItem(str(item_code), 1, 1.0)
              for item_code in range(10)]

print(Order(joe, long_order, LargeOrderPromo()))
print(Order(joe, cart, LargeOrderPromo()))

x = [1, 2, 3, 4, 5, 6, 6, 7]
y = {i for i in x}
print(y)


# =======================================================
# Function Strategy
# =======================================================

from collections import namedtuple
Customer = namedtuple('Customer', 'name fidelity')


class LineItem:

    def __init__(self, product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = price

    def total(self):
        return self.price * self.quantity


class Order:  # the Context

    def __init__(self, customer, cart, promotion=None):
        self.customer = customer
        self.cart = list(cart)
        self.promotion = promotion

    def total(self):
        if not hasattr(self, '__total'):
            self.__total = sum(item.total() for item in self.cart)
        return self.__total

    def due(self):
        if self.promotion is None:
            discount = 0
        else:
            discount = self.promotion(self)
        return self.total() - discount

    def __repr__(self):
        fmt = '<Order total: {:.2f} due: {:.2f}>'
        return fmt.format(self.total(), self.due())


def fidelity_promo(order):
    """5% discount for customers with 1000 or more fidelity points"""
    return order.total() * .05 if order.customer.fidelity >= 1000 else 0


def bulk_item_promo(order):
    """10% discount for each LineItem with 20 or more units"""
    discount = 0
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * .1
    return discount


def large_order_promo(order):
    """7% discount for orders with 10 or more distinct items"""
    distinct_items = {item.product for item in order.cart}
    if len(distinct_items) >= 10:
        return order.total() * .07
    return 0


joe = Customer('John Doe', 0)
ann = Customer('Ann Smith', 1100)

cart = [LineItem('banana', 4, .5),
        LineItem('apple', 10, 1.5),
        LineItem('watermellon', 5, 5.0)]

print(Order(joe, cart, fidelity_promo))
print(Order(ann, cart, fidelity_promo))

banana_cart = [LineItem('banana', 30, .5),
               LineItem('apple', 10, 1.5)]

print(Order(joe, banana_cart, bulk_item_promo))

long_order = [LineItem(str(item_code), 1, 1.0)
               for item_code in range(10)]

print(Order(joe, long_order, large_order_promo))
print(Order(joe, cart, large_order_promo))

promos = [fidelity_promo, bulk_item_promo, large_order_promo]


def best_promo(order):
    """Select best discount available"""
    return max(promo(order) for promo in promos)


print(Order(joe, long_order, best_promo))
print(Order(joe, banana_cart, best_promo))
print(Order(ann, cart, best_promo))

promos = [globals()[name] for name in globals() if name.endswith('_promo') and name != 'best_promo']

#print(globals())

for promo in promos:
    print(promo)

print(best_promo)
print(fidelity_promo)


