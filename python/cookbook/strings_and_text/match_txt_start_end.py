
import os
from urllib.request import urlopen
import re

filename = 'spam.txt'

print(filename.endswith('.txt'))
print(filename.startswith('file:'))

url = 'http://www.python.org'
print(url.startswith('http:'))

filenames = os.listdir('.')

print([name for name in filenames
       if name.endswith(('.py', '.h'))])

print(any(name.endswith('.py') for name in filenames))

# ============================================================

def read_data(name):
    if name.startswith(('http:', 'https:', 'ftp:')):
        return urlopen(name).read()
    else:
        with open(name) as f:
            return f.read()


a = read_data('https://www.facebook.com')
print(a)

# ============================================================

choices = ['http:', 'ftp:']
url = 'http://www.python.org'

try:
    url.startswith(choices)
except TypeError:
    print('Must be tuple, rather than list')
finally:
    try:
        print(url.startswith(tuple(choices)))
    except Exception as e:
        print('Not gonna get here')

# ============================================================

url = 'http://www.python.org'
print(re.match('http:|https:|ftp:', url))

# ============================================================
