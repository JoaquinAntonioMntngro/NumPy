# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 13:29:35 2019

@author: Joaquin
"""

import numpy as np

a = np.linspace(1, 10, 10)
A = a*(a)

b = np.linspace(11, 20, 10)
B = b*b

c = np.linspace(21, 30, 10)
C = c*c

d = np.linspace(31, 40, 10)
D = d*d

e = np.linspace(41, 50, 10)
E = e*e

f = np.linspace(51, 60, 10)
F = f*f

g = np.linspace(61, 70, 10)
G = g*g

h = np.linspace(71, 80, 10)
H = h*h

i = np.linspace(81, 90, 10)
I = i*i

j = np.linspace(91, 100, 10)
J = j*(j)


A = np.array([[A],[B], [C], [D], [E], [F], [G], [H], [I], [J]]).astype(int)
print(A)
print (' ')

x = A%3==0
print (' ')
print("Values divisible by 3: ", x)