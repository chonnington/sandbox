# https://pypi.python.org/pypi/singledispatch

from functools import singledispatch

@singledispatch
def fun(arg, verbose=False):
    if verbose:
        print("Let me just say:", end=" ")
    print(arg)

@fun.register(int)
def _(arg, verbose=False):
    if verbose:
        print("Strength in numbers, eh?", end=" ")
    print(arg)

@fun.register(list)
def _(arg, verbose=False):
    if verbose:
        print("Enumerate this:")
    for i, elem in enumerate(arg):
        print(i, elem-1)

fun("Hello, world.", verbose=True)
fun([1,2,3,4], verbose=True)