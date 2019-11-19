# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 13:29:07 2019

@author: Joaquin
"""

import numpy as np

X = np.random.random((5,5))
print (X)

y = X.mean()
print (' ')
print ("Value of the mean is: ", y)

a = X.std()
print (' ')
print("Value of the standard deviation is: ", a)

Z = (X - y)/a
print (' ')
print ("Value of the normalized X is: ", Z)