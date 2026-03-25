#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Fibonacci:
    """Class for calculating Fibonacci sequence"""
    def __init__(self, n, m):   
        self.n=n
        self.m=m
        
    def fibo_n(self):
        a=0 #setting the initial values
        b=1
        for i in range (2, self.n):
            c=a+b
            a=b
            b=c
        return b
    
    def fibo_list(self):
        fiblist=[] #creating a list to add the fibonacci values to 
        a=0 #setting the initial values
        b=1
        l=2 #setting the initial length of the list 
        while l<(self.n-1): #ensuring that the length of the list is less than N
            if a%self.m==0: #ensuring that the fib number is divisible by M
                fiblist.append(a)
            c=a+b #creating the new fib value which is the sum of the previous two
            a=b #updating the 'previous' values
            b=c
            l+=1
        return fiblist
        
    
fib=Fibonacci(100,7)

print(fib.fibo_n())
print(fib.fibo_list())


# In[ ]:




