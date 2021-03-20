# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 08:12:18 2016

@author: ChonTe01
"""

#from sympy import *
#x, y, z, t = symbols('x y z t')
#k, m, n = symbols('k m n', integer=True)
#f, g, h = symbols('f g h', cls=Function)
#print(x,y,z,t)
#c = Matrix([[1, -1], [3, 4], [0, 2]])
#init_printing(c)

import numpy as np

from numpy.linalg import inv

a = np.array([[3,1,0],[-1,2,2],[5,0,-1]])
print(a)
aInv = inv(a)
print(aInv)
#print(np.dot(a,aInv))
