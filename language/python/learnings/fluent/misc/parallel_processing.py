# -*- coding: utf-8 -*-
from multiprocessing import Pool

def f(x):
    return x*x

if __name__ == '__main__':
    
    p = Pool(5)
    a = [1,2,3,4,5,6,7,8,9,10]
    g = lambda x: x**2
    
    print(p.map(f, a), p.map(g,a))

    for element in a :
        print(f(element))
        print(g(element))
    
    
