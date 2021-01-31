
'''
https://stackoverflow.com/questions/976577/random-hash-in-python
'''

import random
import string


def random_string(length):
    pool = string.letters + string.digits
    return ''.join(random.choice(pool) for i in xrange(length))
