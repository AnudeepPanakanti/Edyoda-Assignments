#!/usr/bin/env python
# coding: utf-8

# In[4]:


def square_num(n):
  return n * n
nums = [4,2,6,8]
print("Original List: ",nums)
result = map(square_num, nums)
print("Square the elements :")
print(list(result))


# In[ ]:




