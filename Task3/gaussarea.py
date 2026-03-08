#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import math
import scipy
import matplotlib.pyplot as plt

a=float(input("Input a value for the lower bound:"))
b=float(input("Input a value for the upper bound:"))
A=float(input("Input a value for A:"))
x0=float(input("Input a value for x0:"))
sigma=float(input("Input a value for sigma:"))
z0=float(input("Input a value for z0:"))

x=np.linspace(-10, 10, 200)

def gauss(x, A, x0, sigma, z0):
    return A*np.exp(-(x-x0)**2/(2*sigma**2))+z0

def gauss2(x):
    return A*np.exp(-(x-x0)**2/(2*sigma**2))+z0

intt=scipy.integrate.quad(gauss2, a, b)

y_values=gauss2(x)
where=(a<=x)&(x<=b)


print(f"The area between x=0 and x=2.5 is equal to {intt}")
print(f"The area between x=-infinty and x=infinity is equal to {intt2}")
plt.plot(x_values, y_values, color='r')
plt.fill_between(x_values[where], y_values[where], label=intt[0])
plt.legend()
plt.show

