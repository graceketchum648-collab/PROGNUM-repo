#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
a=float(input("Input a lower bound:")) #letting teh user choose the lower bound
b=float(input("Input an upper bound:")) #letting the user choose the upper bound
n=int(input("Input a (preferably large) number of points:")) #making them choose a number of data points 
fofx= input("Input a function f(x) using python syntax:") #letting them pick a function
x=np.random.uniform(a, b, n) #choosing x values from a random uniform distribution

y=eval(fofx) #using eval to create a list of all of the values of the function
i=((b-a)/n)*np.sum(y) #evaluating the integral by summing the whole list and applying the monte carlo formula

print(i)

