# -*- coding: utf-8 -*-

import time

from multiprocessing.dummy import Pool as ThreadPool 
from urllib.request import urlopen

def timing(f):
    def wrap(*args):
        time1 = time.time()
        ret = f(*args)
        time2 = time.time()
        print('%s function took %0.3f ms' % (f.__name__, (time2-time1)*1000.0))
        return ret
    return wrap

def setup1():
    urls = [
      'http://www.python.org', 
      'http://www.python.org/about/',
      'http://www.onlamp.com/pub/a/python/2003/04/17/metaclasses.html',
      'http://www.python.org/doc/',
      'http://www.python.org/download/',
      'http://www.python.org/getit/',
      'http://www.python.org/community/',
      'https://wiki.python.org/moin/',
      ]
    
    # make the Pool of workers
    pool = ThreadPool(4) 
    
    # open the urls in their own threads
    # and return the results
    results = pool.map(urlopen, urls)
    
    # close the pool and wait for the work to finish 
    pool.close() 
    pool.join()   

def setup2():
    urls = [
      'http://www.python.org', 
      'http://www.python.org/about/',
      'http://www.onlamp.com/pub/a/python/2003/04/17/metaclasses.html',
      'http://www.python.org/doc/',
      'http://www.python.org/download/',
      'http://www.python.org/getit/',
      'http://www.python.org/community/',
      'https://wiki.python.org/moin/',
      ]

    for url in urls:
        results = urlopen(url)
    
@timing
def main():
    #setup1() # 6615.947 ms
    setup2()


main()



