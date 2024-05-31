#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd


# In[6]:


car=pd.read_csv('quikr_car.csv')


# In[7]:


car.head()


# In[5]:


car.shape


# In[7]:


car.info()


# In[8]:


car['year'].unique()


# In[11]:


car['Price'].unique()


# In[12]:


car['kms_driven'].unique()


# In[8]:


car['fuel_type'].unique()


# In[9]:


backup=car.copy()


# In[10]:


car=car[car['year'].str.isnumeric()]


# In[11]:


car['year']=car['year'].astype(int)


# In[12]:


car.info()


# In[32]:


car['Price']


# In[33]:


car[car['Price']!="Ask for Price"]


# In[34]:


car=car[car['Price']!="Ask for Price"]


# In[35]:


car['price']

