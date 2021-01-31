
def chain(*iterables):
    for it in iterables:
        for i in it:
            yield i


s = 'ABC'
t = tuple(range(3))
u = 'UVA'

print(list(chain(s, t, u)))


def chain(*iterables):
    for i in iterables:
        yield from i


print(list(chain(s, t, u)))

