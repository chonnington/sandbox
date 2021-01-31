# -*- coding: utf-8 -*-
from math import sqrt

def F(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return F(n-1)+F(n-2)

def F(n):
    return ((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5))
    
f = lambda x: x**4 - 14*x**3 + 60*x**2 - 70*x

fxRange = [0,2]
fxR = max(fxRange) - min(fxRange)
