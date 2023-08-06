#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Step 1: Import the dataset using Pandas from the given URL.
url = 'https://raw.githubusercontent.com/SR1608/Datasets/main/covid-data.csv'
df = pd.read_csv('https://raw.githubusercontent.com/SR1608/Datasets/main/covid-data.csv')
# Step 2: High-Level Data Understanding
# a. Find the number of rows & columns in the dataset
num_rows, num_cols = df.shape
print("Number of rows:", num_rows)
print("Number of columns:", num_cols)

# b. Check the data types of columns
data_types = df.dtypes
print(data_types)

# c. Display info & description of data in the dataframe
print(df.info())
print(df.describe())

# Step 3: Low-Level Data Understanding
# a. Find the count of unique values in the 'location' column
unique_locations = df['location'].nunique()
print("Number of unique locations:", unique_locations)

# b. Find which continent has the maximum frequency using value counts
continent_max_freq = df['continent'].value_counts().idxmax()
print("Continent with maximum frequency:", continent_max_freq)

# c. Find the maximum & mean value in the 'total_cases' column
max_total_cases = df['total_cases'].max()
mean_total_cases = df['total_cases'].mean()
print("Maximum total cases:", max_total_cases)
print("Mean total cases:", mean_total_cases)

# d. Find the 25%, 50%, and 75% quartile value in the 'total_deaths' column
quartiles_total_deaths = df['total_deaths'].quantile([0.25, 0.5, 0.75])
print("25% quartile value:", quartiles_total_deaths[0.25])
print("50% quartile value:", quartiles_total_deaths[0.5])
print("75% quartile value:", quartiles_total_deaths[0.75])

# e. Find which continent has the maximum 'human_development_index'
continent_max_hdi = df.loc[df['human_development_index'].idxmax(), 'continent']
print("Continent with maximum human development index:", continent_max_hdi)

# f. Find which continent has the minimum 'gdp_per_capita'
continent_min_gdp = df.loc[df['gdp_per_capita'].idxmin(), 'continent']
print("Continent with minimum GDP per capita:", continent_min_gdp)

# Step 4: Filter the dataframe with only the specified columns and update the dataframe
columns_to_keep = ['continent', 'location', 'date', 'total_cases', 'total_deaths', 'gdp_per_capita', 'human_development_index']
df = df[columns_to_keep]

# Step 5: Data Cleaning
# a. Remove all duplicate observations
df.drop_duplicates(inplace=True)

# b. Find missing values in all columns
missing_values = df.isnull().sum()
print(missing_values)

# c. Remove all observations where the 'continent' column value is missing
df.dropna(subset=['continent'], inplace=True)

# d. Fill all missing values with 0
df.fillna(0, inplace=True)

# Step 6: Date Time Format
# a. Convert the 'date' column to datetime format using pandas.to_datetime
df['date'] = pd.to_datetime(df['date'])

# b. Create a new column 'month' after extracting the month data from the 'date' column
df['month'] = df['date'].dt.month

# Step 7: Data Aggregation
# a. Find the max value in all columns using groupby function on the 'continent' column
df_groupby = df.groupby('continent').max()
print(df_groupby)

# Step 8: Feature Engineering
# a. Create a new feature 'total_deaths_to_total_cases' by the ratio of 'total_deaths' column to 'total_cases'
df_groupby['total_deaths_to_total_cases'] = df_groupby['total_deaths'] / df_groupby['total_cases']

# Step 9: Data Visualization
# a. Perform Univariate analysis on the 'gdp_per_capita' column by plotting a histogram using seaborn distplot
sns.distplot(df['gdp_per_capita'])
plt.title('Histogram of GDP per Capita')
plt.show()

# b. Plot a scatter plot of 'total_cases' & 'gdp_per_capita'
plt.scatter(df['total_cases'], df['gdp_per_capita'])
plt.xlabel('Total Cases')
plt.ylabel('GDP per Capita')
plt.title('Scatter Plot: Total Cases vs. GDP per Capita')
plt.show()

# c. Plot a Pairplot on df_groupby dataset
sns.pairplot(df_groupby)
plt.show()

# d. Plot a bar plot of the 'continent' column with 'total_cases'
sns.catplot(x='continent', y='total_cases', kind='bar', data=df)
plt.title('Total Cases by Continent')
plt.show()

# Step 10: Save the 'df_groupby' dataframe to the local drive using pandas.to_csv function
df_groupby.to_csv('df_groupby.csv')


# In[ ]:



