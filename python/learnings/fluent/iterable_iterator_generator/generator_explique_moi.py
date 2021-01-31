# def gen_123():
#     yield 1
#     yield 2
#     yield 3
#
# print(gen_123) # doctest: +ELLIPSIS
#
#
# for i in gen_123():
#     print(i)
#
#
# g = gen_123()
#
# print(next(g))
# print(next(g))
# print(next(g))
#
# try:
#     print(next(g))
# except StopIteration as e:
#     print('wtf')


# def gen_AB():
#     print('start')
#     yield 'A'
#     print('continue')
#     yield 'B'
#     print('end.')
#
#
# i = 0
# for c in gen_AB():
#     print(i, '-->', c)
#     i += 1

'''

The generator function is defined like any function, but uses yield.

'''

import re
import reprlib

RE_WORD = re.compile('\w+')


class Sentence:

    def __init__(self, text):
        self.text = text

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

    def __iter__(self):
        print('sup im iteraing first')
        for match in RE_WORD.finditer(self.text):
            yield match.group()


a = Sentence('yuit foh shizzler qwevec quo toi nycverisic')

print(a)

for b in a:
    print(b)






