#!/usr/bin/env python
# coding: utf-8

# In[1]:


s={1,2,3,4,5,6,7,8,9,10}
print(s,type(s))


# In[3]:


s={1,2,3,4,5,6,7,8,9,10}
s.add(12)
print(s,type(s))
s.pop()
print(s,type(s))


# In[6]:


s1={1,2,3,4,5}
s2={2,4,6,8,10}
s3=s1.union(s2)
print(s3,type(s3))
s4=s1.intersection(s2)
print(s4,type(s4))
s5=s1.difference(s2)
print(s5,type(s5))
s6=s1.symmetric_difference(s2)
print(s6,type(s6))


# In[7]:


squares={x**2 for x in range(1,11)}
print(squares)


# In[14]:


s={1,2,3,4,5,6,7,8,9,10}
s={x for x in range(1,11) if x%2==0}
print(s)


# In[16]:


s={1,2,3,1,3,4,5,6,7,4,2,8,7,9,10}
print(s,type(s))
s.remove(2)
s.remove(1)
s.remove(3)
s.remove(7)
s.remove(4)
print(s,type(s))


# In[20]:


s1={1,2,3,4,5}
s2={1,2,3}
print(s2.issubset(s1))
print(s1.issuperset(s2))


# In[25]:


fs=({1,2,3,4,5})
print(fs,type(fs))
fset=frozenset(fs)
print(fset,type(fset))


# In[26]:


s1={1,2,3,4,5}
list1=list(s1)
list1.append(6)
print(list1,type(list1))
s2=set(list1)
print(s2,type(s2))


# In[2]:


x={1:10,2:20,3:30}
print(x,type(x))


# In[29]:


s1={10,20+3j,"Python",40.87,True}
print(s1,type(s1))
for val in s1:
    print(val,type(val))


# In[30]:


s1={10,20,30,40,50,60}
print(s1,type(s1))
s1.pop()
print(s1)
s1.pop()
print(s1)
s1.pop()
print(s1)
s1.pop()
print(s1)
s1.pop()
print(s1)
s1.pop()
print(s1)


# In[32]:


s1={1,2,3,4,5,6}
print(s1,type(s1))
s2={5,6,7,8,9,10}
print(s2,type(s2))
s1=s1.symmetric_difference(s2)
print("symmetric_wdiffernce of two sets:",s1,type(s1))


# In[33]:


s={15,"python",2+3j,True}
print(s,type(s))
print(15 in s)
print(True in s)


# In[34]:


s1={(1,2),(3,4),(5,6),(7,8)}
print(s1,type(s1))


# In[ ]:




