#!/usr/bin/env python
# coding: utf-8

# In[3]:


D= float (input("Enter a day:"))
M= int(input("Enter a month:"))
Y= int(input("Enter a year:"))


JD = 367*Y -7*(Y+(M+9)//12)/4 - 3*((Y+(M-9)//7)//100 + 1)//4 + (275*M)//9 + D + 1721029-0.5
print (f"The Julien Date corresponding to the data given is {JD} days.")


# In[ ]:




