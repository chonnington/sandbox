
'''
def f1(a):
    print(a)
    print(b)
b = 6
f1(3)
'''

'''
b = 6
def f2(a):
    print(a)
    print(b)
    # b = 9
f2(3)
'''

'''
b = 6
def f3(a):
    global b
    print(a)
    print(b)
    b = 9

f3(3)
print(b)

a = 3
print(b)
b = 8
b = 30
print(b)
'''



def make_pow(n):
    def fixed_exponent_pow(x):
        return pow(x, n)
    def foo(x):
        return x
    return fixed_exponent_pow

sqr = make_pow(2)
print(sqr(10))