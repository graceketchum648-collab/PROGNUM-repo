#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
from numpy import sin, cos, exp, pi
import math
import scipy

fofx = input("Input a function f(x) using python syntax: ")

try: #having a try except clause so that the bounds have to be numbers
    a = eval(input("Input a lower bound: "))
    b = eval(input("Input an upper bound: "))
except Exception:
    print("Oops! Your bounds did not use valid numbers, try again!")
    exit()

if a >= b: #so that the monte carlo integration expression can work
    print("Lower bound must be smaller than upper bound.")
    exit()

n=10000 #number of data points 

x=np.random.uniform(a, b, n) #choosing x values from a random uniform distribution

try:
    f = lambda x: eval(fofx) #making it so that fofx is evaluated with x as the variable
    f(1)   # test evaluation
except Exception:
    print("Oops! You need to use valid python syntax for your function. Try again...")
    exit()

intt = scipy.integrate.quad(f, a, b) #using quad to integrate

y = eval(fofx)
inttmc=((b-a)/n)*sum(y) #using the monte carlo expression to integrate

print(intt)
print(inttmc)

