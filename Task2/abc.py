#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from math import sqrt
a= float(input("Enter the value for a:"))
b= float(input("Enter the value for b:"))
c= float(input("Enter the value for c:"))

D= (b**2)-4*a*c
if D>0:
    x1= (-b+(sqrt(D)))/2*a
    x2= (-b-(sqrt(D)))/2*a
    print(f"The two solutions of the second degree polynomial are {x1} and {x2}")
elif D==0:
    x= -b/(2*a)
    print(f"The single solution of the second degree polynomial is {x}")
else:
    print("No solutions can be found")


