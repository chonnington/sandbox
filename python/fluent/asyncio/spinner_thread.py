import threading
import itertools
import time
import sys


class Signal:
    go = True


def spin(msg, signal):
    write, flush = sys.stdout.write, sys.stdout.flush
    print('get out my face')
    for char in itertools.cycle('|/-\\'):
        status = char + ' ' + msg
        write(status)
        flush()
        write('\x08' * len(status))
        time.sleep(.1)
        if not signal.go:
            print('im broke!')
            break
    write(' ' * len(status) + '\x08' * len(status))


def slow_function():
    time.sleep(3)
    return 42


def supervisor():
    signal = Signal()
    spinner = threading.Thread(target=spin,
                               args=('thinking!', signal))
    print('spinner objectL', spinner)
    spinner.start()
    print('yolo')
    result = slow_function()
    print('bear')
    signal.go = False
    spinner.join()
    return result


def main():
    result = supervisor()
    print('Answer: ', result)


if __name__ == '__main__':
    main()