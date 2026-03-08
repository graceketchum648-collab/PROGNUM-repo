#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import math
import scipy
import matplotlib.pyplot as plt
A = 1.0 #setting the initial conditions
x0 = 0.0
sigma = 2.0
z0 = 0.0
x=np.linspace(-10, 10, 200)

def gauss(x, A, x0, sigma, z0): #defining teh function
    return A*np.exp(-(x-x0)**2/(2*sigma**2))+z0

def gauss2(x): #making it so that x is teh only variable we use i the integration
    return A*np.exp(-(x-x0)**2/(2*sigma**2))+z0

intt=scipy.integrate.quad(gauss2, 0, 2.5) #integrating from 0 to 2.5
intt2=scipy.integrate.quad(gauss2, -np.inf, np.inf) #integrating from negative infinity to infinity 

x_values=x
y_values=gauss2(x)
where=(0<=x)&(x<=2.5) #making it so that the appropriate area can be filled in


print(f"The area between x=0 and x=2.5 is equal to {intt}")
print(f"The area between x=-infinty and x=infinity is equal to {intt2}")
plt.plot(x_values, y_values, color='r')
plt.fill_between(x_values[where], y_values[where])
plt.show


#part 2
area1=A*sigma*(2*math.pi)**(1/2) #using the formula
print(f"The calculated area under the curve is {area1}, which is equal to the are evaluated using quad()")

