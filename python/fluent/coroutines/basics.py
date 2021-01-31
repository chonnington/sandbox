def simple_coroutine():
    print('-> coroutine started')
    x = yield
    print('-> coroutine received', x)


# my_coro = simple_coroutine()
# print(my_coro)
# print(next(my_coro))
# try:
#     my_coro.send(42)
# except StopIteration:
#     print('no more')


#
# my_coro = simple_coroutine()
#
# try:
#     my_coro.send(1729)
# except:
#     print("can't send non-None value to a just-started generator")
# print('==='*10)

'''
The initial call next(my_coro) is often described as “priming” the coroutine, 
i.e. advancing it to the first yield to make it ready for use as a live coroutine.
'''


from inspect import getgeneratorstate


def simple_coro2(a):
    print('-> Started: a =', a)
    b = yield a
    print('-> Received: b =', b)
    c = yield a + b
    print('-> Received: c =', c)


# my_coro2 = simple_coro2(14)
# print(getgeneratorstate(my_coro2))
#
# next(my_coro2)
# my_coro2.send(28)
#
# try:
#     my_coro2.send(99)
# except Exception as e:
#     print(e)
# finally:
#     print(getgeneratorstate(my_coro2))


# def averager1():
#     total = 0.0
#     count = 0
#     average = None  # 0 works as well
#     while True:
#         term = yield average
#         total += term
#         count += 1
#         average = total/count


# approach 1 of priming
# next(coro_avg)
# print(coro_avg.send(10))
# print(coro_avg.send(30))
# print(coro_avg.send(5))


from coroaverager1 import averager

coro_avg = averager()

print(coro_avg.send(40))
print(coro_avg.send(41))

'''
>>> coro_avg.send('spam') # Traceback (most recent call last):
...
TypeError: unsupported operand type(s) for +=: 'float' and 'str' >>> coro_avg.send(60) #
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
'''

