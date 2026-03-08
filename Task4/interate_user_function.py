#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
from numpy import sin, cos, exp, pi
import math
import scipy

fofx = input("Input a function f(x) using python syntax: ")

try:
    a = eval(input("Input a lower bound: "))
    b = eval(input("Input an upper bound: "))
except Exception:
    print("Oops! Your bounds did not use valid numbers, try again!")
    exit()

if a >= b:
    print("Lower bound must be smaller than upper bound.")
    exit()

n=10000 #number of data points 

x=np.random.uniform(a, b, n) #choosing x values from a random uniform distribution

try:
    f = lambda x: eval(fofx)
    f(1)   # test evaluation
except Exception:
    print("Oops! You need to use valid python syntax for your function. Try again...")
    exit()

intt = scipy.integrate.quad(f, a, b) #using eval to create a list of all of the values of the function

y = eval(fofx)
inttmc=((b-a)/n)*sum(y)

print(intt)
print(inttmc)

