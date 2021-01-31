# spinner_asyncio.py

# credits: Example by Luciano Ramalho inspired by
# Michele Simionato's multiprocessing example in the python-list:
# https://mail.python.org/pipermail/python-list/2009-February/538048.html

# BEGIN SPINNER_ASYNCIO
import asyncio
import itertools
import sys


@asyncio.coroutine  # <1>
def spin(msg):  # <2>
    write, flush = sys.stdout.write, sys.stdout.flush
    for char in itertools.cycle('|/-\\'):
        status = char + ' ' + msg
        write(status)
        flush()
        write('\x08' * len(status))
        try:
            yield from asyncio.sleep(.1)  # <3>
        except asyncio.CancelledError:  # <4>
            break
    write(' ' * len(status) + '\x08' * len(status))


@asyncio.coroutine
def slow_function():  # <5>
    # pretend waiting a long time for I/O
    yield from asyncio.sleep(3)  # <6>
    print('3 seconds')
    return 42

@asyncio.coroutine
def slow_function2():
    yield from asyncio.sleep(5)
    print('5 seconds')


@asyncio.coroutine
def supervisor():  # <7>
    spinner = asyncio.async(spin('thinking!'))  # <8>
    print('spinner object:', spinner)  # <9>
    result = yield from slow_function()  # <10>
    yield from slow_function2()
    print('8 [s]')
    spinner.cancel()  # <11>
    return result


def main():
    loop = asyncio.get_event_loop()  # <12>
    result = loop.run_until_complete(supervisor())  # <13>
    loop.close()
    print('Answer:', result)


if __name__ == '__main__':
    main()


'''
Never use time.sleep(...) in asyncio coroutines unless you want to block the main thread, 
therefore freezing the event loop and prob‐ ably the whole application as well. 
If a coroutine needs to spend some time doing nothing, it should yield from asyncio.sleep(DELAY).
'''