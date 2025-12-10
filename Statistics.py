#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd
df=pd.DataFrame({"x":[1,1,2,5,4,3],"y":[1,1,2,3,4,4],"z":[1,1,2,2,3,3],"i":[5.0,1.0,3.0,4.0,2.0,1.0]})
df


# In[8]:


df["x"].mean()


# In[9]:


df["x"].median()


# In[10]:


df["x"].mode()


# In[11]:


df["y"].mean()


# In[12]:


df["y"].median()


# In[13]:


df["y"].mode()


# In[14]:


df["z"].mean()


# In[15]:


df["z"].median()


# In[16]:


df["z"].mode()


# In[17]:


df["i"].mean()


# In[18]:


df["i"].median()


# In[19]:


df["i"].mode()


# In[26]:


df["x-μ"] = df["x"] - df["x"].mean()
df["x-μ"].mean()


# In[27]:


df["x"].max()


# In[28]:


df["x"].min()


# In[29]:


df["x"].max()-df["x"].min()


# In[32]:


import pandas as pd
import numpy as np
df=pd.DataFrame({"x":[10,11,12,25,25,27,31,33,34,36,54,59]})
df


# In[33]:


df["x"].quantile(0)


# In[34]:


df["x"].min()


# In[35]:


q1=df["x"].quantile(0.25)
q1


# In[36]:


q2=df["x"].quantile(0.5)
q2


# In[37]:


q3=df["x"].quantile(0.75)
q3


# In[38]:


q4=df["x"].quantile(1)
q4


# In[40]:


df["x"].quantile([0,0.25,0.5,0.75,1])


# In[41]:


df["x"].describe()


# In[43]:


iqr=q3-q1
iqr


# In[45]:


l=np.random.randint(1,100,10).tolist()
l.sort()
print(l)


# In[47]:


ll=q1-(iqr*1.5)
ll


# In[48]:


ul=q3+(iqr*1.5)
ul


# In[51]:


df[(df["x"]<ll)]|df[(df["x"]<ul)]


# In[56]:


import seaborn as sns
sns.boxplot(df["x"])
plot.show()


# In[ ]:




