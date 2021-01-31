'''
def d1(fn):
    def foo():
        return '<F>' + fn() + '<F>'
    return foo

def d2(fn):
    def bar():
        return '<>' + fn() + '<>'
    return bar

@d1
@d2
def f():
    return 'terry'


a = f()
print(a)
'''

'''
def f():
    print('f')
    
f = d1(d2(f))
'''


registry = set()
def register(active=True):
    def decorate(func):
        print('running register(active=%s)->decorate(%s)' % (active, func))
        if active:
            registry.add(func)
        else:
            registry.discard(func)
        return func
    return decorate

@register(active=False)
def f1():
    print('running f1()')

@register(active=True)
def f2():
    print('running f2()')

def f3():
    print('running f3()')

print()
print(registry)

print()
register()(f3)

print()
print(registry)

print()
register(active=False)(f2)

print()
print(registry)