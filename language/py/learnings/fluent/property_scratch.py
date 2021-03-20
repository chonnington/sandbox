
'''
class Silly:

    def _get_silly(self):
        print("You are getting silly")
        return self._silly

    def _set_silly(self, value):
        print("You are making silly {}".format(value))
        self._silly = value

    def _del_silly(self):
        print("Whoah, you killed silly!")
        del self._silly

    silly = property(_get_silly,
                     _set_silly,
                     _del_silly,
                     "This is a silly property")

s = Silly()
s.silly = "funny"
s.silly
del s.silly
'''

'''
class Foo:
    @property
    def foo(self):
        return "bar"


class Foo1:

    @property
    def foo(self):
        return self._foo

    @foo.setter
    def foo(self, value):
        print('setting foo value')
        self._foo = value


a = Foo1()
a.foo = 25
'''

import time

from urllib.request import urlopen


class WebPage:

    def __init__(self, url):
        self.url = url
        self._content = None
        self._content2 = None

    @property
    def content(self):
        if not self._content:
            print("Retrieving New Page...")
            self._content = urlopen(self.url).read()
            print(self._content)
        else:
            print('content present')
        return self._content

    @property
    def content2(self):
        print('invoked')
        if not self._content2:
            self._content2 = 'foobar'
        return self._content2

    
class StaticWebPage:

    def __init__(self, url):
        self.url = url
        self.foo = None

    def content(self):
        if not self.foo:
            self.foo = 'bar'
        return self.foo


webpage = WebPage("http://ccphillips.net/")

now = time.time()
content1 = webpage.content
print(time.time() - now)

now = time.time()
content2 = webpage.content
print(time.time() - now)

print(webpage.content2)

static_webpage = StaticWebPage("www.google.com")
print(static_webpage.content())
