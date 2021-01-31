import time

def clock(func):
    def clocked(*args): #
        print(args)
        t0 = time.perf_counter()
        result = func(*args) #
        elapsed = time.perf_counter() - t0
        name = func.__name__
        arg_str = ', '.join(repr(arg) for arg in args)
        print('[%0.8fs] %s(%s) -> %r' % (elapsed, name, arg_str, result))
        return result
    return clocked #



factorial_memo = {}

@clock
def factorial(k):
    if k < 2: return 1
    if k not in factorial_memo:
        factorial_memo[k] = k * factorial(k-1)
    return factorial_memo[k]

