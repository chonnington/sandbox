from inspect import getgeneratorstate


class DemoException(Exception):

    """An exception type for the demonstration."""


def demo_exc_handling():
    print('-> coroutine started')
    while True:
        try:
            x = yield
        except DemoException:
            print('*** DemoException handled. Continuing...')
        else:
            print('-> coroutine received: {!r}'.format(x))
    raise RuntimeError('This line should never run.')


exc_coro = demo_exc_handling()

next(exc_coro)
exc_coro.send(1525)
exc_coro.send('que va pillar?!')
exc_coro.close()
print(getgeneratorstate(exc_coro))

print('=='*20)

exc_coro = demo_exc_handling()
next(exc_coro)
exc_coro.send(11)
exc_coro.throw(DemoException)
print(getgeneratorstate(exc_coro))
