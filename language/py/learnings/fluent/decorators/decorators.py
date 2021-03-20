
'''

@decorate
def target():
    print('running target()')
    
Has the same effect as writing this:
def target():
    print('running target()')
target = decorate(target)

'''


def deco(func):
    def inner():
        print('running inner()')
    return inner

@deco
def target():
    print('running target()')

target()