#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np

# 1. Create a null vector of size 10 but the fifth value which is 1.
null_vector = np.zeros(10)
null_vector[4] = 1
print("Null vector with 1 at the fifth position:")
print(null_vector)

# 2. Create a vector with values ranging from 10 to 49.
vector_10_to_49 = np.arange(10, 50)
print("Vector with values ranging from 10 to 49:")
print(vector_10_to_49)

# 3. Create a 3x3 matrix with values ranging from 0 to 8
matrix_3x3 = np.arange(9).reshape(3, 3)
print("3x3 matrix with values ranging from 0 to 8:")
print(matrix_3x3)

# 4. Find indices of non-zero elements from [1,2,0,0,4,0]
array = np.array([1, 2, 0, 0, 4, 0])
non_zero_indices = np.nonzero(array)
print("Indices of non-zero elements:")
print(non_zero_indices)

# 5. Create a 10x10 array with random values and find the minimum and maximum values.
random_array = np.random.random((10, 10))
min_value = np.min(random_array)
max_value = np.max(random_array)
print("Random 10x10 array:")
print(random_array)
print("Minimum value:", min_value)
print("Maximum value:", max_value)

# 6. Create a random vector of size 30 and find the mean value.
random_vector = np.random.random(30)
mean_value = np.mean(random_vector)
print("Random vector of size 30:")
print(random_vector)
print("Mean value:", mean_value)


# In[ ]:




