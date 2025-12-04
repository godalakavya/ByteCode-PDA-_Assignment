#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd


# In[13]:


import pandas as pd

df = pd.read_excel(os.path.join(os.path.expanduser("~"), "Desktop", "sample_data.xlsx"), engine="openpyxl")
df.head()


# In[27]:


df.head()
df.info()
df.describe()
df.shape


# In[15]:


import pandas as pd
import os

csv_path = os.path.join(os.path.expanduser("~"), "Desktop", "sample_data.csv")
df_csv = pd.read_csv(csv_path)

df_csv


# In[28]:


df_csv.info()


# In[30]:


#Data Selection & Slicing (IMPORTANT)
df[["Name", "City"]]


# In[31]:


df["Salary"]


# In[33]:


df.loc[0]     # by label


# In[34]:


df.iloc[0]    # by index


# In[36]:


#Filtering with Conditions
df[df["Salary"] > 50000]


# In[37]:


df[(df["Age"] > 22) & (df["City"] == "Bangalore")]


# In[40]:


df[df["City"].isin(["Mumbai", "Delhi"])]


# In[39]:


#Explore the Dataset (Basic EDA)-commands
df.head()
df.tail()
df.shape
df.info()
df.describe()
df.columns
df.index


# In[6]:


import pandas as pd
df={"Age":[22,30,23,44,54],
    "Salary":[17000,18000,20000,32000,15000],
    "Gender":['f','f','m','m','f']}
df=pd.DataFrame(df)
df


# In[7]:


df.drop(index=0)


# In[8]:


df.drop(index=[1,2])


# In[10]:


df.drop(columns='Age')


# In[11]:


df.drop(columns=['Age','Gender'])


# In[13]:


df.iloc[:,0]=[30,12,34,65,38]
df


# In[14]:


df.iloc[0,:]=1
df


# In[15]:


df.iloc[[0,2],0]=10
df


# In[16]:


df.iloc[[0,2],:]=[[20,10000,'M'],[40,37000,'f']]
df


# In[17]:


df.iloc[3,1]=46000
df


# In[20]:


import numpy as np
df.iloc[:,0]=[30,32,np.nan,38,40]
df


# In[22]:


df.iloc[3,[0,1]]=np.nan
df


# In[24]:


df.iloc[2,[1,2]]=np.nan
df


# In[25]:


df.iloc[[1,2],2]=np.nan
df


# In[26]:


df["Age_N"]=[25,33,87,54,23]
df


# In[27]:


df.loc[5]=[36,50000,'f',55]
df


# In[32]:


df["ABC"]=list(range(11,17))
df


# In[ ]:




