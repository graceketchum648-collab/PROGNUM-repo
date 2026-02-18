#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Sirius data
apparentMagnitude = input("Enter the apparent magnitude: ")
absoluteMagnitude = input("Enter the absolute magnitude: ")



# The distance is related to the magnitudes as m-M=5.Log(d/10)
# 1 Parsec = 3.26164 ly

m = float(apparentMagnitude)
M = float(absoluteMagnitude)

d = 10.0 * pow( 10.0, (m-M)/5.0 ) * 3.26164
print (f"The distance is {d} light years")


# In[ ]:




