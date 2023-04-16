#!/usr/bin/env python
# coding: utf-8

# In[2]:


def upperlower(string):
 
    upper = 0
    lower = 0
 
    for i in range(len(string)):
         
        # For lower letters
        if (ord(string[i]) >= 97 and
            ord(string[i]) <= 122):
            lower += 1
 
        # For upper letters
        elif (ord(string[i]) >= 65 and
            ord(string[i]) <= 90):
            upper += 1
 
    print('Lower case characters = %s' %lower)
    print('Upper case characters = %s' %upper)
 

string = input("Enter the input : ")
upperlower(string)


# In[ ]:




