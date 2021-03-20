# -*- coding: utf-8 -*-

# https://jeffknupp.com/blog/2016/03/07/python-with-context-managers/

#==============================================================================
'''
class File():

    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        print('im entering')
        self.open_file = open(self.filename, self.mode)
        return self.open_file

    def __exit__(self, *args):
        print('im exiting')
        self.open_file.close()

files = []
for i in range(10):
    with File('foo.txt', 'a') as infile:
        infile.write('foo' + str(i))
        files.append(infile)

for file in files:
    print(file)
'''

#==============================================================================

'''
from threading import Lock
lock = Lock()

def do_something_dangerous():
    with lock:
        raise Exception('oops I forgot this code could raise exceptions')

try:
    do_something_dangerous()
except:
    print('Got an exception')
lock.acquire()
print('Got here')
'''

#==============================================================================

'''
Everything before the call to yield 
is considered the code for __enter__(). 

Everything after is the code for __exit__().
'''

'''
from contextlib import contextmanager

@contextmanager
def open_file(path, mode):
    the_file = open(path, mode)
    yield the_file
    the_file.close()

files = []

for x in range(100):
    with open_file('foo.txt', 'w') as infile:
        files.append(infile)

for f in files:
    if not f.closed:
        print('not closed')
'''

#==============================================================================
        
from contextlib import contextmanager

@contextmanager
def tag(name):
    print("<%s>" % name)
    yield
    print("</%s>" % name)

with tag("h1"):
    print("foo")

#==============================================================================
    
from contextlib import ContextDecorator

class makeparagraph(ContextDecorator):
    def __enter__(self):
        print('<p>')
        return self

    def __exit__(self, *exc):
        print('</p>')
        return False

@makeparagraph()
def emit_html():
    print('Here is some non-HTML')

emit_html()
    
    






