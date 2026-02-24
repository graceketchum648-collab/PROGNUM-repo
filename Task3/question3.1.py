#!/usr/bin/env python
# coding: utf-8

# In[ ]:


masses = [1.9891e+30, 1.8986e+27, 
          5.6846e+26, 1.0243e+26, 8.6810e+25,
          5.9736e+24, 4.8685e+24, 6.4185e+23, 
          3.3022e+23, 7.349e+22, 1.25e22]

moon= 7.349e+22
masses_1= []

for num in masses:
    if num > moon:
        masses_1.append(num) #creating a new list without the masses smalller or equal to tat of the moon
print(masses_1)

last_5=masses[-5:] #reducing the list to the last 5 of the og list
print(last_5)

s= sum(last_5)
l=len(last_5)
average=s/l

print(average)

