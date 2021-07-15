#!/usr/bin/env python
# coding: utf-8

# # Topic : Exploratory Data Analysis - Retail
# # Author : Hemangi Jakharia
# # Task : Exploratory Data Analysis On Superstore Dataset

# # Import Libraries

# In[3]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from warnings import filterwarnings
filterwarnings(action='ignore')


# # Loading Datasets

# In[4]:


data = pd.read_csv("Downloads/SampleSuperstore.csv")
data.head()


# In[5]:


print(data.shape)


# # Description of dataset

# In[6]:


data.describe()


# # Checking Null Datasets

# In[7]:


data.isna().sum()


# In[8]:


#Dropping duplicates
data.drop_duplicates(keep="first",inplace = True)


# In[9]:


data.corr()


# In[10]:


data.groupby('Ship Mode').mean()


# In[11]:


data.groupby('Segment').mean()


# In[12]:


corr = data.corr()
sns.heatmap(corr,annot=True)


# In[13]:


sns.countplot(data['Segment'])
plt.show()


# In[14]:


sns.countplot(data['State'])
plt.show()


# In[15]:


plt.plot(data['Sales'])
plt.show()


# In[16]:


data.hist(figsize=(10,10),bins=50)
plt.show()


# In[17]:


sns.pairplot(data,hue='Segment');


# In[18]:


plt.figure(figsize=(10,8))
data['Sub-Category'].value_counts().plot.pie(autopct='%1.1f%%')
plt.show()


# In[19]:


plt.figure(figsize=(5,8))
data['Region'].value_counts().plot.pie(autopct='%1.1f%%')
plt.show()


# In[20]:


data1 = data[['City','Category', 'State','Sales','Profit']]
# pandas pivot with multiple variables
heatmap1_data = pd.pivot_table(data1,values='Sales', index=["City"], columns='Category')


# # Heatmap of sales in every city by category¶

# In[21]:


plt.figure(figsize=(8, 12))
sns.heatmap(heatmap1_data, cmap="BuGn")


# # Heatmap of sales in every State by category

# In[22]:


heatmap2_data = pd.pivot_table(data1,values='Sales', index=["State"], columns='Category')
plt.figure(figsize=(8, 12))
sns.heatmap(heatmap2_data, cmap="BuGn")


# # Heat map of profits in every state by category

# In[23]:


heatmap3_data = pd.pivot_table(data1,values='Profit', index=["State"], columns='Category')
plt.figure(figsize=(8, 12))
sns.heatmap(heatmap3_data, cmap="BuGn")


# # Heatmap of profit in every city by category

# In[24]:


heatmap4_data = pd.pivot_table(data1,values='Profit', index=["City"], columns='Category')
plt.figure(figsize=(8, 12))
sns.heatmap(heatmap4_data, cmap="BuGn")


# # Heatmap of profit in every city by segment

# In[25]:


heatmap5_data = pd.pivot_table(data,values='Profit', index=["City"], columns='Segment')
plt.figure(figsize=(8, 12))
sns.heatmap(heatmap5_data, cmap="BuGn")


# # Heatmap of profits in every state by segment

# In[26]:


heatmap6_data = pd.pivot_table(data,values='Profit', index=["State"], columns='Segment')
plt.figure(figsize=(8, 12))
sns.heatmap(heatmap6_data, cmap="BuGn")


#  # Heatmap of sales in every city by sub-category

# In[28]:


heatmap7_data = pd.pivot_table(data,values='Sales', index=["City"], columns='Sub-Category')
plt.figure(figsize=(8, 12))
sns.heatmap(heatmap7_data, cmap="BuGn")


# # Heatmap of profit in every city by sub-category

# In[30]:


heatmap8_data = pd.pivot_table(data,values='Profit', index=["City"], columns='Sub-Category')
plt.figure(figsize=(8, 12))
sns.heatmap(heatmap8_data, cmap="BuGn")


# In[31]:


plt.figure(figsize=(11,11))
data.groupby('Sub-Category')['Profit','Sales'].agg(['sum']).plot.bar()
plt.show()


# In[ ]:




