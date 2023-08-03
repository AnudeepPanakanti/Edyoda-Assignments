#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Step 1: Import the necessary libraries
import pandas as pd

# Step 2: Create the DataFrame with the given values
raw_data = {
    'regiment': ['Nighthawks', 'Nighthawks', 'Nighthawks', 'Nighthawks', 'Dragoons', 'Dragoons', 'Dragoons', 'Dragoons', 'Scouts', 'Scouts', 'Scouts', 'Scouts'], 
    'company': ['1st', '1st', '2nd', '2nd', '1st', '1st', '2nd', '2nd','1st', '1st', '2nd', '2nd'], 
    'name': ['Miller', 'Jacobson', 'Ali', 'Milner', 'Cooze', 'Jacon', 'Ryaner', 'Sone', 'Sloan', 'Piger', 'Riani', 'Ali'], 
    'preTestScore': [4, 24, 31, 2, 3, 4, 24, 31, 2, 3, 2, 3],
    'postTestScore': [25, 94, 57, 62, 70, 25, 94, 57, 62, 70, 62, 70]
}

regiment = pd.DataFrame(raw_data)

# Step 3: From each regiment, what is the mean preTestScore?
mean_preTestScore_regiment = regiment.groupby('regiment')['preTestScore'].mean()
print("Mean preTestScore by regiment:")
print(mean_preTestScore_regiment)

# Step 4: Present general statistics by company
statistics_by_company = regiment.groupby('company')['preTestScore'].describe()
print("\nGeneral statistics by company:")
print(statistics_by_company)

# Step 5: What is the mean of each company's preTestScore?
mean_preTestScore_company = regiment.groupby('company')['preTestScore'].mean()
print("\nMean preTestScore by company:")
print(mean_preTestScore_company)

# Step 6: Present the mean preTestScores grouped by regiment and company
mean_preTestScore_grouped = regiment.groupby(['regiment', 'company'])['preTestScore'].mean()
print("\nMean preTestScore grouped by regiment and company:")
print(mean_preTestScore_grouped)

# Step 7: Present the mean postTestScores grouped by regiment and company
mean_postTestScore_grouped = regiment.groupby(['regiment', 'company'])['postTestScore'].mean()
print("\nMean postTestScore grouped by regiment and company:")
print(mean_postTestScore_grouped)

# Step 8: Group the entire dataframe by regiment and company
grouped_data = regiment.groupby(['regiment', 'company'])
print("\nGrouped DataFrame:")
print(grouped_data.head())

# Step 9: What is the number of observations in each regiment and company?
num_observations = grouped_data.size()
print("\nNumber of observations in each regiment and company:")
print(num_observations)


# In[ ]:




