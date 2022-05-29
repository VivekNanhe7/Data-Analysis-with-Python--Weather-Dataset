#!/usr/bin/env python
# coding: utf-8

# # The Weather Dataset

# Here , the weateher dataset is Time-Series data set with per-hour information about the Weather conditions at a particular Location.

# It records Temperature, Dew point temperature, Realative humidity, Wind speed, Visibility, Pressure and Conditions.

# This data is available as a CSV file. we are going to analyze this data set using the Pandas DataFrame.

# In[1]:


import pandas as pd


# In[2]:


data = pd.read_csv(r'C:\Users\vivek\NumPy\Data Science Projects\weather dataset.csv')


# In[3]:


data


# # How to Analyze DataFrames?

# ## .head() - It shows the first N number of rows

# In[4]:


data.head(5)


# ## .shape() - shows the number of rows and columns

# In[6]:


data.shape


# ## .index - provides the index of dataset

# In[7]:


data.index


# ## .columns - shows the name of each column

# In[10]:


data.columns


# ## .dtypes - shows the datatype of each column

# In[11]:


data.dtypes


# ## .unique() - In a column, it shows all the unique values. it can be applied on single column only, not on the whole dataframe.

# In[19]:


data['Wind Speed_km/hr'].unique


# ## .nunique() - it show the total number of unique values in each column. it can be applied on a single column as well as on whole dataframe.

# In[21]:


data.nunique()


# ## .count - it shows the total no. of non-null values in each column. apply on single column as well as whole dataframe

# In[22]:


data.count


# ## .value_counts - In a column, shows all the unique values with their count. applied on single column only

# In[25]:


data['Weather'].value_counts()


# ## .info() - provide information about dataframe

# In[26]:


data.info()

