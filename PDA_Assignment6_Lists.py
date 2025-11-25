#!/usr/bin/env python
# coding: utf-8

# In[2]:


l1=list(range(1,21))
print(l1,type(l1))


# In[3]:


print("first element:",l1[0])
print("last element:",l1[19])
print("middle element:",l1[9])


# In[13]:


print("first element:",l1[0:5])
print("last element:",l1[15:21])
print("middle element:",l1[5:15])


# In[26]:


l1=[1,2,3,4,5,6,7,8,9,10]
squares = [i*i for i in range(1, 11)]
print(squares,type(squares))


# In[28]:


l1=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
even_numbers = [i for i in range(1, 21) if i % 2 == 0]
print(even_numbers)


# In[34]:


l1=[1,2,8,6,22,38,76,3,2,90,65,32,55,10,11,22,90,65]
print(l1,type(l1))
l1.sort(reverse=False)
print(l1,type(l1))
l1.sort(reverse=True)
print(l1,type(l1))
unique_list=list(set(l1))
unique_list.sort(reverse=False)
print(unique_list,type(unique_list))


# In[37]:


mat=[(1,2,3),(4,5,6),(7,8,9)]
print("the list matrix is")
for val in mat:
    print(val)
print("the element at the second row and third column ",mat[1][2])


# In[1]:


students = [
    {"name": "Kavya", "score": 85},
    {"name": "Ravi", "score": 92},
    {"name": "Anu", "score": 78},
    {"name": "Teja", "score": 90}
]
sorted_students = sorted(students, key=lambda x: x['score'], reverse=True)
print(sorted_students)


# In[2]:


def transpose_matrix(matrix):
    return [[matrix[j][i] for j in range(3)] for i in range(3)]
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
transposed = transpose_matrix(matrix)
print("Original Matrix:")
for row in matrix:
    print(row)
print("\nTransposed Matrix:")
for row in transposed:
    print(row)


# In[1]:


l1=[[1,2,3],[4,5,6],[7,8,9]]
print("original list is:",l1,type(l1))
l2=[]
for val in l1:
    for v in val:
        l2.append(v)
print("flattend list is:",l2,type(l2))


# In[4]:


numbers = list(range(1, 11))
for index in sorted([2, 4, 6], reverse=True):
    numbers.pop(index)
numbers.insert(5, 99)
print("Modified List:", numbers)


# In[6]:


list1 = [10, 20, 30, 40, 50]
list2 = ['x', 'y', 'z', 'p', 'q']
combined = list(zip(list1, list2))
print("Combined List of Tuples:")
print(combined)


# In[7]:


def reverse_list(lst):
    return lst[::-1]  
original = [1, 2, 3, 4, 5]
reversed_list = reverse_list(original)
print("Original List:")
print(original)
print("\nReversed List:")
print(reversed_list)


# In[2]:


l=[10,20,30,40,50,60,70,80,90]
print(l,type(l))
n=int(input("Enter number of positions n:"))
l1=l[n:]
l2=l[:n]
l3=l1+l2
print(l3,type(l3))


# In[9]:


def intersect_lists(list1, list2):
    return [item for item in list1 if item in list2]
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7]
intersection = intersect_lists(list1, list2)
print("List 1:", list1)
print("List 2:", list2)
print("\nIntersected List:", intersection)


# In[ ]:




