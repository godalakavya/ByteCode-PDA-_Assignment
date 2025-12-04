#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
arr = np.random.randint(1, 21, (5, 5))
arr[:, 2] = 1
print(arr)


# In[3]:


arr = np.arange(1, 17).reshape(4, 4)
np.fill_diagonal(arr, 0)
print(arr)


# In[7]:


arr = np.arange(1, 37).reshape(6, 6)
sub1 = arr[2:5, 1:4]
sub2 = arr[3:5, 2:4]
print(sub1)
print(sub2)


# In[3]:


import numpy as np
a=np.random.randint(1,20,[5,5])
print(a)
print("elements in the border")
for i in range(len(a)):
    for j in range(len(a[i])):
        if i==0 or i==len(a)-1 or j==0 or j==len(a[i])-1:
            print(a[i,j],end=" ")


# In[5]:


#Create two NumPy arrays of shape (3, 4) filled with random integers. Perform element-wise addition, subtraction, multiplication, and division.
a=np.random.randint(1,20,[3,4])
b=np.random.randint(1,20,[3,4])
print(a)
print(b)
print("addition a+b:")
print(a+b)
print("subtraction a-b:")
print(a-b)
print("multiplication a*b:")
print(a*b)
print("division a/b:")
print(a/b)


# In[6]:


#Create a NumPy array of shape (4, 4) with values from 1 to 16. Compute the row-wise and column-wise sum.
a=np.arange(1,17)
a=a.reshape((4,4))
print(a)
for i in range(4):
    rsum=0
    csum=0
    for j in range(4):
        rsum+=a[i,j]
        csum+=a[j,i]
    print(i,"row wise sum is:",rsum)
    print(i,"column wise sum of is:",csum)


# In[7]:


#Create two NumPy arrays of shape (2, 3) and (3, 2). Perform matrix multiplication on these arrays.
a=np.array([[1,2,3],[4,5,6]])
b=np.array([[1,2],[3,4],[5,6]])
print(a)
print(b)
print(np.matmul(a,b))


# In[8]:


#Create a NumPy array of shape (3, 3) with values from 1 to 9. Reshape the array to shape (1, 9) and then to shape (9, 1).
a=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a)
a=a.reshape((1,9))
print(a)
a=a.reshape((9,1))
print(a)


# In[9]:


#Create a NumPy array of shape (5, 5) filled with random integers. Flatten the array and then reshape it back to (5, 5).
a=np.random.randint(1,100,[5,5])
print(a)
print(np.ravel(a))
print(a.reshape((5,5)))


# In[10]:


#Create a NumPy array of shape (5, 5) filled with random integers. Use fancy indexing to extract the elements at the corners of the array.
a=np.random.randint(1,100,[5,5])
print(a)
print("The elements at the corners of the array")
print(a[0,:],a[:,0],a[4,:],a[:,4])


# In[12]:


#Create a NumPy array of shape (4, 4) filled with random integers. Use boolean indexing to set all elements greater than 10 to 10.
a=np.random.randint(-100,100,[5,5])
print(a)
a[a>10]=10
print(a)


# In[ ]:




