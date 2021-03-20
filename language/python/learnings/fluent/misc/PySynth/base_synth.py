# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 08:03:51 2017

@author: tchon
"""

import pysynth as ps

test = (('c', 4), ('e', 4), ('g', 4),
		('c5', -2), ('e6', 8), ('d#6', 2))
ps.make_wav(test, fn = "test.wav")