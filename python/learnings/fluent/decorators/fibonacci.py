import functools

from clockdeco import clock

@clock
def fibonacci1(n):
    if n < 2:
        return n
    return fibonacci1(n-2) + fibonacci1(n-1)

@functools.lru_cache() #
@clock #
def fibonacci2(n):
    if n < 2:
        return n
    return fibonacci2(n-2) + fibonacci2(n-1)

if __name__=='__main__':
    print()
    print(fibonacci1(5))
    print()
    print(fibonacci2(5))