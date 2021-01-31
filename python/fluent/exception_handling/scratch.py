
'''
def no_return():
    print("I am about to raise an exception")
    raise Exception("This is always raised")
    print("This line will never execute")
    return "I won't be returned"

def call_exceptor():
    print("call_exceptor starts here...")
    no_return()
    print("an exception was raised...")
    print("...so these lines don't run")

try:
    no_return()
except:
    print("I caught an exception")
print("executed after the exception")
'''

'''
def funny_division(divider):
    try:
        return 100 / divider
    except (ZeroDivisionError, TypeError):
        return "Enter a number other than zero"

print()
print('1)', funny_division(0))
print('2)', funny_division(50.0))
print('3)', funny_division("hello"))

print()
for val in (0, "hello", 50.0, 13):
    print("Testing [{}]: ".format(val), end=" ")
    print(funny_division(val))

'''

'''
def funny_division3(anumber):
    try:
        if anumber == 13:
            raise ValueError("13 is an unlucky number")
        return 100 / anumber
    except ZeroDivisionError:
        return "Enter a number other than zero"
    except TypeError:
        return "Enter a numerical value"
    except ValueError:
        print("No, No, not 13!")
        raise

funny_division3(13)
'''

'''
try:
    raise ValueError("This is an argument")
except ValueError as e:
    print("The exception arguments were", e.args)
'''

'''
import random

some_exceptions = [ValueError, TypeError, IndexError, None]

try:
    choice = random.choice(some_exceptions)
    print(choice)
    print("raising {}".format(choice))
    if choice:
        raise choice()
except ValueError:
    print("Caught a ValueError")
except TypeError:
    print("Caught a TypeError")
except Exception as e:
    print("Caught some other error: %s" % ( e.__class__.__name__))
else:
    print("This code called if there is no exception")
finally:
    print("This cleanup code is always called")
'''

'''
class InvalidWithdrawal(Exception):
    pass

raise InvalidWithdrawal("You don't have $50 in your account")
'''

'''
class InvalidWithdrawal(Exception):
    def __init__(self, balance, amount):
        super().__init__("account doesn't have ${}".format(amount))
        self.amount = amount
        self.balance = balance
        self.overage()

    def overage(self):
        return self.amount - self.balance

# raise InvalidWithdrawal(250, 50)

try:
    raise InvalidWithdrawal(25, 50)
except InvalidWithdrawal as e:
    print("I'm sorry, but your withdrawal is "
          "more than your balance by "
          "${}".format(e.overage()))

def divide_with_exception(number, divisor):
    try:
        print("{} / {} = {}".format(number, divisor, number / divisor * 1.0))
    except ZeroDivisionError:
        print("You can't divide by zero")

def divide_with_if(number, divisor):
    if divisor == 0:
        print("You can't divide by zero")
    else:
    print("{} / {} = {}".format(number, divisor, number / divisor * 1.0))
'''

class Inventory:
    def lock(self, item_type):
        '''Select the type of item that is going to
        be manipulated. This method will lock the
        item so nobody else can manipulate the
        inventory until it's returned. This prevents
        selling the same item to two different
        customers.'''
        pass
    def unlock(self, item_type):
        '''Release the given type so that other
        customers can access it.'''
        pass
    def purchase(self, item_type):
        '''If the item is not locked, raise an
        exception. If the item_type does not exist,
        raise an exception. If the item is currently
        out of stock, raise an exception. If the item
        is available, subtract one item and return
        the number of items left.'''
        pass
    

class InvalidItemType(Exception):
    def __init__(self):
        super().__init__("damn it")
    pass

class OutOfStock(Exception):
    pass

item_type = 'widget'
inv = Inventory()
inv.lock(item_type)

try:
    num_left = inv.purchase(item_type)
except InvalidItemType:
    print("Sorry, we don't sell {}".format(item_type))
except OutOfStock:
    print("Sorry, that item is out of stock.")
else:
    print("Purchase complete. There are "
          "{} {}s left".format(num_left, item_type))
finally:
    inv.unlock(item_type)