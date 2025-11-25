#!/usr/bin/env python
# coding: utf-8

# In[1]:


t1=(1,2,3,4,5,6,7,8,9,10)
print(t1,type(t1))


# In[2]:


print("First element:", t1[0])
print("Middle element:", t1[len(t1)//2 - 1])  
print("Last element:", t1[-1])


# In[4]:


print("first three elements:",t1[:3])
print("last three elements:",t1[-3:])
print("elements from index 2 to 5:",t1[2:6])


# In[30]:


mat=((1,2,3),(4,5,6),(7,8,9))
print("the tuple matrix is")
for val in mat:
    print(val)
print("the element at the second row and third column ",mat[1][2])


# In[15]:


t1=(1,2,3)
t2=(4,5,6)
t3=t1+t2
print("Concatenate tuple:",t3)


# In[27]:


t1=(1,2,3,1,6,4,3,8,9,7,2,7,4)
t1.count(1)
t2.count(7)
print("the index of first occurence of 3 is:",t1.count(3)) 
print("the index of first occurence of 9 is:",t1.count(9)) 


# In[31]:


t1=1,2,3,4,5
a,b,c,d,e=t1
print(a,b,c,d,e)


# In[35]:


l1=[1,2,3,4,5]
print(l1,type(l1))
l1.append(6)
print(l1,type(l1))
t1=tuple(l1)
print(t1,type(t1))


# In[37]:


l1=[1,2,3,4,5]
t1=tuple(l1)
print(t1,type(t1))


# In[1]:


t=((10,20,30),(40,50,60),(70,80,90))
print("The tuple is",t)
print("The tuple of tuples is")
for val in t:
    print(val)


# In[2]:


t="P","Y","T","H","O","N"
print("The tuple is",t,type(t))
s=""
for char in t:
    s=s+char
print("Tuple elemnets into a string is",s,type(s))


# In[3]:


d={1:"a",2:"b",3:"c",4:"d"}
print(d,type(d))


# In[4]:


t=(1,2,3),(4,5,6),(7,8,9)
print(t,type(t))
for val in t:
    for element in val:
        print(element)


# In[5]:


t1=1,4,5,4,9,5,7,1,5,6,7,2,5
print(t1,type(t))
s=set(t1)
print("The resultant set is",s,type(s))


# In[6]:


t1=1,4,5,4,9,5,7,1,5,6,0,7,2,5
t2=(min(t1),max(t1),sum(t1))
print(t2)
for val in t2:
    print(val)


# In[ ]:




