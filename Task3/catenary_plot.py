#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import matplotlib.pyplot as plt
import math

x_values=range(-5, 6) #starts at -4 in order to exclude -5
def shape(x):
    shape=math.cosh(x)
    return shape
y_values= [shape(x) for x in x_values]

plt.plot(x_values, y_values, label="Catenary")
plt.title("Catenary")
plt.grid()
plt.ylabel("Hyperbolic cosine")
plt.xlabel("Values of x")
plt.xticks(x_values)
plt.yticks(range(-1, 75, 5))
plt.legend()
plt.show

