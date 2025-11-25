#!/usr/bin/env python
# coding: utf-8

# In[1]:


d1={1:1,2:4,3:9,4:16,5:25,6:36,7:49,8:64,9:81,10:100}
print(d1,type(d1))


# In[9]:


d1[5]
print(d1[5])
for k,v in d1.items():
    print(k)


# In[28]:


d1={1:1,2:4,3:9,4:16,5:25,6:36,7:49,8:64,9:81,10:100}
d2={11:121}
d1.update(d2)
print(d1,type(d1))
d1.pop(1,1)
print(d1,type(d1))


# In[30]:


d1={1:1,2:4,3:9,4:16,5:25,6:36,7:49,8:64,9:81,10:100}
for k,v in d1.items():
    print(k,"-->",v)


# In[35]:


d1={1:1,2:4,3:9,4:16,5:25,6:36,7:49,8:64,9:81,10:100}
cubes_dict = {i: i**3 for i in range(1, 11)}
print(cubes_dict,type(cubes_dict))


# In[36]:


d1={1:1,2:4,3:9,4:16,5:25}
d2={6:36,7:49,8:64,9:81,10:100}
d1.update(d2)
print(d1,type(d1))


# In[39]:


d1={"name":"kavya","age":21,"grades":{"math":30,"science":40,"english":32}}
print(d1,type(d1))
for k,v in d1["grades"].items():
    print(k,"-->",v,type(v),type(d1))
    


# In[40]:


d1={1: [1, 2, 3, 4, 5], 2: [2, 4, 6, 8, 10], 3: [3, 6, 9, 12, 15], 4: [4, 8, 12, 16, 20], 5: [5, 10, 15, 20, 25]}
print(d1,type(d1))
for k,v in d1.items():
    print(k,"-->",v,type(v),type(d1))


# In[41]:


d1={1:(1,1),2:(2,4),3:(3,9),4:(4,16),5:(5,25)}
print(d1,type(d1))
for k,v in d1.items():
    print(k,"-->",v,type(v),type(d1))


# In[43]:


d1={1:1,2:4,3:9,4:16,5:25}
list_of_tuples = list(d1.items())
print(list_of_tuples)


# In[44]:


d1={1:1,2:4,3:9,4:16,5:25,6:36,7:49,8:64,9:81,10:100}
even_keys_dict = {i: square for i, square in d1.items() if i % 2 == 0}
print(even_keys_dict)


# In[45]:


d1={1:1,2:4,3:9,4:16,5:25}
swapped_dict = {value: key for key, value in d1.items()}
print(swapped_dict)


# In[1]:


key=['a','b','c']
val=[]
d=dict.fromkeys(key,val)
print("default dictionary is",d,type(d))
val.append(1)
val.append(2)
print("resultant dictionary is",d,type(d))


# In[2]:


def countchar(s):
    d={}
    for char in s:
        d[char]=s.count(char)
    return d
s='mississippi'
print(countchar(s),type(countchar(s)))


# In[3]:


book={'title':'Ram chandra series','author':'Manish','year':2021,'genre':11}
print(book,type(book))


# In[ ]:




