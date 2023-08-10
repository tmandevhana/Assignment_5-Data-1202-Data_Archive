#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# import pandas as pd

# Load dataset 1
df1 = pd.read_csv('Zimbabwe - Data on forcibly displaced populations1.csv')
df1.head()


# In[3]:


# Load dataset 2
df2 = pd.read_csv('Zimbabwe Data on forced Displacements by year  - 2020.csv')
df2.head()


# In[5]:


# Load dataset 1 and replace missing values with a specific value (e.g., 0)
df1 = pd.read_csv('Zimbabwe - Data on forcibly displaced populations1.csv')
df1.fillna(0, inplace=True)  # Replace NaN with 0


# In[6]:


df1.head()


# In[9]:


# Load dataset 2 and replace missing values with a specific value (e.g., 0)
df2.fillna(0, inplace=True)  # Replace NaN with 0


# In[17]:


df2.head()


# In[21]:


print(df1['Year'].dtype)
print(df2['Year'].dtype)


# In[31]:


# Convert the 'Year' column to integers, replacing empty values with NaN
df1['Year'] = pd.to_numeric(df1['Year'], errors='coerce')
df1 = df1.dropna(subset=['Year'])
df1['Year'] = df1['Year'].astype(int)

# Convert the 'Year' column to integers, replacing empty values with NaN
df2['Year'] = pd.to_numeric(df2['Year'], errors='coerce')
df2 = df2.dropna(subset=['Year'])
df2['Year'] = df2['Year'].astype(int)

# Perform the merge operation based on the 'Year' column
merged_df = pd.merge(df1, df2, on='Year')

# Display the merged DataFrame
print(merged_df.head())


# In[32]:


print("Unique Years in df1:", df1['Year'].unique())
print("Unique Years in df2:", df2['Year'].unique())


# In[33]:


# Concatenate the two DataFrames vertically
merged_df = pd.concat([df1, df2])

# Display the merged DataFrame
print(merged_df.head())


# In[ ]:




