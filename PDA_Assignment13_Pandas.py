#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[5]:


#Part A Data Selection
#1. Create a DataFrame df with 10 rows and 5 columns containing random integers from 1 to 100
df=pd.DataFrame({
   'A':np.random.randint(1,100,10),
   'B':np.random.randint(1,100,10),
   'C':np.random.randint(1,100,10),
   'D':np.random.randint(1,100,10)
    })
df


# In[7]:


df.iloc[2,1]


# In[9]:


df[['A','C']]


# In[10]:


df.loc[:,['A','C']]


# In[11]:


df.iloc[:,[0,2]]


# In[12]:


#c. Select multiple rows [2, 4, 7] and all columns.
df.loc[[2,4,7],:]


# In[13]:


df.iloc[[2,4,7],:]


# In[14]:


#d. Select rows [1, 3, 5] and columns ['B', 'D'].
df.loc[[2,4,7],['B','D']]


# In[15]:


df.iloc[[2,4,7],[1,3]]


# In[16]:


#Part B: Data Modification 2. Using the same DataFrame df: 
#a. Add a new column E with values [10,20,...] corresponding to row numbers.
df['E']=list(range(10,101,10))
df


# In[17]:


#b. Remove the column C.
df.drop(columns='C')


# In[18]:


#c. Replace all values in column B with 0.
df['B']=0
df


# In[19]:


#d. Replace row 4 with [1,2,3,4,5]
df.iloc[4]=[1,2,3,4,5]
df


# In[20]:


#d. Replace row 4 with [1,2,3,4,5]
df.iloc[4]=[1,2,3,4,5]
df


# In[21]:


#e. Replace rows [2,5] in column A with 99
df.loc[[2,5],'A']=99
df


# In[22]:


df.iloc[[2,5],0]=99
df


# In[23]:


#f. Replace rows [0,1,2] with [ [1,1,1,1,1], [2,2,2,2,2], [3,3,3,3,3] ].
df.iloc[[0,1,2],:]=[[1,1,1,1,1],[2,2,2,2,2],[3,3,3,3,3]]
df


# In[24]:


df.loc[[0,1,2],:]=[[1,1,1,1,1],[2,2,2,2,2],[3,3,3,3,3]]
df


# In[25]:


#Part C: Deleting Values 3. 
#a. Delete a single value in the DataFrame by setting it to NaN.
df.iloc[0,0]=np.nan
df


# In[26]:


#b. Drop row 3 entirely. 
df.drop(index=3)


# In[27]:


#c. Drop column D.
df.drop(columns='D')


# In[28]:


#d. Drop multiple columns ['B', 'E']. 
df.drop(columns=['B','E'])


# In[29]:


#e. Drop multiple rows [0,2,5].
df.drop(index=[0,2,5])


# In[30]:


#d. Drop multiple columns ['B', 'E']. 
df.drop(columns=['B','E'])


# In[31]:


#e. Drop multiple rows [0,2,5].
df.drop(index=[0,2,5])


# In[32]:


#Part D: Mathematical Operations 4. 
#a. Add 10 to all values in column A. 
df['A']+10


# In[33]:


#b. Multiply column B by 2. 
df['B']*2


# In[34]:


#c. Calculate the sum of row 5
sum(df.iloc[5,:])


# In[35]:


sum(df.loc[5,:])


# In[36]:


# d. Calculate the mean of all columns.
print(df['A'].mean())
print(df['B'].mean())
print(df['C'].mean())
print(df['D'].mean())


# In[37]:


#Part E: Conditional Selection 5. 
#a. Extract all rows where column A > 50.
df[df['A']>50]


# In[38]:


#b. Extract all rows where column B < 30 and column D > 10. 
df[(df['B']<30)&(df['D']>10)]


# In[39]:


#c. Replace all values in column C where value < 50 with 0.
df[df['C']<50]
df


# In[40]:


#Part F: Bonus / Advanced 6. 
#a.Replace multiple rows and multiple columns with a single value (e.g.,replace rows [1,2] and columns ['B','D'] with 999).
df.loc[[1,2],['B','D']]=999
df


# In[41]:


df.iloc[[1,2],[1,3]]=999
df


# In[42]:


#7. b. Replace multiple rows and multiple columns with different values.
df.loc[[1,2],['B','D']]=[10,20],[30,40]
df


# In[43]:


df.iloc[[1,2],[1,3]]=[10,20],[30,40]
df


# In[44]:


#8. c. Extract values using iloc and loc for specific positions and labels.
df.loc[:,['A','B','C','D']]


# In[45]:


df.iloc[:,[0,1,2,3]]


# In[46]:


df.iloc[:,:]


# In[47]:


df[['A','C','D','B']]


# In[48]:


df.set_index('A')


# In[49]:


df.reset_index()
df


# In[50]:


df


# In[ ]:




