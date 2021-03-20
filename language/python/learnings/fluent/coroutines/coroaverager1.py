
from coroutil import coroutine

@coroutine
def averager():
    total, count = 0.0, 0
    average = None
    while True:
        term = yield average
        total += term
        count += 1
        average = total/count