import re
import reprlib

from collections import abc

RE_WORD = re.compile('\w+')


class Sentence:

    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)
        print(self.words)

    def __getitem__(self, index):
        return self.words[index]

    # def can_i_count_it_off(self):
    #     for word, number in zip(self.words, range(len(self.words))):
    #         print(word, number)

    def __len__(self):
        return len(self.words)

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

    # def __iter__(self):
    #     return SentenceIterator(self.words)

    def __iter__(self):
        for word in self.words:
            yield word
        # return


# class SentenceIterator:
#
#     def __init__(self, words):
#         self.words = words
#         self.index = 0
#
#     def __next__(self):
#         try:
#             word = self.words[self.index]
#         except IndexError:
#             raise StopIteration()
#             self.index += 1
#         return word
#
#     def __iter__(self):
#         return self


# sentence1 = Sentence('wsup wsup hello darkness my new friend?')
# print(sentence1[5])
# sentence1.can_i_count_it_off()



# for word in s: print(word)


'''
The iter built-in function:

1. Checks whether the object implements, __iter__, and calls that to obtain an iterator;

2. If __iter__ is not implemented, but __getitem__ is implemented, Python creates an iterator that attempts to fetch items in order, starting from index 0 (zero);

3. If that fails, Python raises TypeError, usually saying "'C' object is not iterable", where C is the class of the target object.

Why any Python sequence is iterable: they all implement __getitem__. 
'''

# class Foo:
#     def __iter__(self):
#         pass
#
#
# s = Sentence('"The time has come," the Walrus said,') #
#
# print(issubclass(Foo, abc.Iterable))
# f = Foo()
# print(isinstance(f, abc.Iterable))
# print(issubclass(Sentence, abc.Iterable))

'''

Python obtains iterators from iterables.

Here is a simple for loop iterating over a str. The str 'ABC' is the iterable here. You
don’t see it, but there is an iterator behind the curtain:
'''


# s = 'ABC'
# for char in s:
#     print(char)
#
#
# s = 'WSUP'
# it = iter(s) #
#
# while True:
#     try:
#         print(next(it)) #
#     except StopIteration: #
#         print('DAMN')
#         del it #
#         break #


print('wsup wsup')
a = Sentence('wsup wsup')

for i in a:
    print('sup', i)

'''

It may be tempting to implement __next__ in addition to __iter__ in the Sentence
class, making each Sentence instance at the same time an iterable and iterator over
itself. But this is a terrible idea. It’s also a common anti-pattern, according to Alex Mar‐
telli who has a lot of experience with Python code reviews.


Use the Iterator pattern

• to access an aggregate object’s contents without exposing its internal representation.
• to support multiple traversals of aggregate objects.
• to provide a uniform interface for traversing different aggregate structures (that is,to support polymorphic iteration)


An iterable should never act as an iterator over itself. In other words,
iterables must implement __iter__, but not __next__.

On the other hand, for convenience, iterators should be iterable. An
iterator’s __iter__ should just return self.

'''