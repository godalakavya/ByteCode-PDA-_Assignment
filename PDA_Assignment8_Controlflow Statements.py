#!/usr/bin/env python
# coding: utf-8

# In[1]:


num=eval(input("Enter a number: "))
if num>0:
    print("number is positive")


# In[2]:


num=eval(input("Enter a number: "))
if num>0:
    print("number is positive")
elif num<0:
    print("number is negative")


# In[3]:


num=eval(input("Enter a number: "))
if num>0:
    print("number is positive")
elif num<0:
    print("number is negative")
else:
    print("number is zero")


# In[4]:


num=eval(input("Enter a number: "))
if num>0:
    print("number is positive")
    if num%2==0:
        print("number is even")
    else:
        print("number is odd")
elif num<0:
    print("number is negative")


# In[5]:


for n in range(1,11):
    print(n)


# In[6]:


n=1
while(n<=10):
    print(n)
    n+=1


# In[7]:


for _ in range(1,6):
    for _ in range(1,6):
        print('*',end='')
    print()


# In[ ]:


sum=0
while(True):
    n=eval(input("enter a number: "))
    sum+=n
    if n==0:
        break
print(sum)


# In[1]:


for n in range(1,11):
    if n==5:
        continue
    print(n)


# In[14]:


def empty_fun() :
    pass
empty_fun
print("The program run successfully")


# In[12]:


num=int(input("Enter a number: "))
for n in range(1,num+1):
    if n%2==0:
        print(n)


# In[9]:


n=int(input("Enter a number: "))
i=1
prod=1
while(i<=n):
    prod*=i
    i+=1
print("factorial of",n,"is",prod)


# In[5]:


n=int(input("Enter a number: "))
sum=0
while(n>0):
    r=n%10
    sum+=r
    n=n//10
print("sum of digits is",sum)


# In[6]:


n=int(input("Enter a number: "))
count=0
for i in range(2,n):
    if n%i==0:
        count+=1
if count==0:
    print("number is prime")
else:
    print("number is not prime")


# In[8]:


f=0
s=1
n=int(input("Enter a number: "))
count=0
while(count<n):
    print(f)
    sum=f+s
    f=s
    s=sum
    count+=1


# In[ ]:




