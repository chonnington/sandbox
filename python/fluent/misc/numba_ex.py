# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 20:40:52 2017

@author: MrChonnington
"""

from numba import jit
from numpy import arange

# jit decorator tells Numba to compile this function.
# The argument types will be inferred by Numba when function is called.
@jit
def sum2d(arr):
    M, N = arr.shape
    result = 0.0
    for i in range(M):
        for j in range(N):
            result += arr[i,j]
    return result
import time

st = time.time()
a = arange(9).reshape(3,3)
print(sum2d(a))
    
