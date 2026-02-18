#!/usr/bin/env python
# coding: utf-8

# In[1]:


k=1
n=2
i=3
while i<100:
    g=n+k #the value of the fibonacci term
    k=n #setting k as the second previous value
    n=g #setting n as the previous value
    i=i+1 #adding a number of terms

print(f"The 100th Fibonnacci term has a value of {g}")


# In[ ]:




