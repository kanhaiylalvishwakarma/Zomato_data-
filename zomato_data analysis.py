#!/usr/bin/env python
# coding: utf-8

# # Zomato data analysis project

# # Step-1 importing library

# In[4]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[3]:


df=pd.read_csv('Zomato data .csv')
df


# # convert the data type of column_rate

# In[5]:


def handleRate(value):
    value =str(value).split('/')
    value=value[0];
    return float(value)
df['rate']=df['rate'].apply(handleRate)
print(df.head())


# In[6]:


df.info()


# # Type of resturant

# In[7]:


df.head()


# In[12]:


sns.countplot(x=df['listed_in(type)'])
plt.xlabel("type of resturant")                  


# # conclusion-majority of the resturant falls in dinning category

# In[13]:


df.head()


# In[16]:


grouped_data=df.groupby('listed_in(type)')['votes'].sum()
result= pd.DataFrame({'votes':grouped_data})
plt.plot(result,c="green",marker="o")
plt.xlabel("type of resturant",c="red",size=20)
plt.ylabel("votes",c="red",size=20)


# # conclusion-dinning resturants has recived maximum votes

# In[17]:


df.head()


# In[19]:


plt.hist(df['rate'],bins=5)
plt.title('rating distribution')
plt.show


# # conclusion-the majority resturants recived rating from 3.5 to 4.5

# # average order spending by couple

# In[20]:


df.head()


# In[21]:


couple_data=df['approx_cost(for two people)']
sns.countplot(x=couple_data)


# # conclusion- the majority of couples preferr resturent with an approximate cost of 300rupees

# # which mode recevies maximum rating

# In[22]:


plt.figure(figsize=(6,6))
sns.boxplot(x='online_order',y='rate',data=df)


# # conclusion-offline order received lower rating in comparision to online order

# In[31]:


pivot_table= df.pivot_table(index='listed_in(type)',columns='online_order',aggfunc='size',fill_value=0)
sns.heatmap(pivot_table,annot=True,cmap="YlGnBu",fmt='d')
plt.title("Heatmap")
plt.xlabel("online_order")
plt.ylabel("Listed In (type)")
plt.show()


# # conclusion-Dining resturents primarily accept offline orders, whereas cafes primarily receive online order.This suggests that clients prefer orders in person at resturents,but prefer online ordering at cafes.

# In[ ]:




