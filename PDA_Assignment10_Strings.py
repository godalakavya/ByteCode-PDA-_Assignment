#!/usr/bin/env python
# coding: utf-8

# In[1]:


s = "hello"
print(s)
print(type(s))


# In[4]:


s = "hello"
print(length(s))


# In[5]:


s = "hello"
print(len(s))


# In[6]:


s1 = "hello"
s2 = "hello"
print(id(s1))
print(id(s2))


# In[7]:


s1 = "hello"
s2 = "hello"
print(s1 is s2)


# In[8]:


s1 = "hello"
s2 = "hello"
s3 = "hi"
print(s1 is s2)
print(s2 is s3)


# In[9]:


s1 = "hello"
s2 = "hello"
s3 = "hi"
print(s1 == s2)
print(s2 == s3)


# In[10]:


print("a" + "bc")


# In[11]:


print("abcd"[2:])


# In[12]:


str1 = 'hello'
str2 = ','
str3 = 'world'
print(str1[-1:])


# In[13]:


print(r"\nhello")


# In[14]:


print('new' 'line')


# In[15]:


str1="helloworld"
print(str1[::-1])


# In[16]:


example = "snow world"
example[3] = 's'
print(example)


# In[17]:


l = [1, 2, 3]
print(min(l))
print(max(l))


# In[18]:


q="what are you"
print(min(q))
print(max(q))


# In[19]:


example="hello"
print(example.count("l"))


# In[20]:


example = "helle"
print(example.find("e"))


# In[21]:


example = "helle"
print(example.rfind("e"))


# In[22]:


example="helloworld"
print(example[::0])


# In[23]:


str1="restart"
char = str1[0]
str1 = str1.replace(char, '$')
print(str1)


# In[24]:


str1="restart"
char = str1[0]
str1 = str1.replace(char, '$')
str2 = char + str1[1:]
print(str2)


# In[25]:


example="helloworld"
print(example[::-1].startswith("d"))


# In[26]:


print("hello\example\test.txt")


# In[27]:


print("hello\\example\\test.txt")


# In[28]:


print("hello\"example\"test.txt")


# In[29]:


print("hello"\example"\test.txt")


# In[30]:


print("hello"+1+2+3)


# In[31]:


print("D", end = ' ')
print("C", end = ' ')
print("B", end = ' ')
print("A", end = ' ')


# In[32]:


print("Hello".replace("l", "e"))


# In[33]:


print("abc DEF".capitalize())


# In[34]:


print("abcdef".upper())


# In[35]:


print("ABCDEF".upper())


# In[36]:


print("ABCDEFG".lower())


# In[37]:


print("abcdef".center())


# In[38]:


print("xyyzxyzxzxyy".count('yy'))


# In[39]:


print("xyyzxyzxzxyy".count('yy', 1))


# In[40]:


print("xyyzxyzxzxyy".count('yy', 4))


# In[41]:


print("xyyzxyzxzxyy".endswith("xyy"))


# In[42]:


print("ab\tcd\tef")


# In[43]:


print("a\nb")


# In[44]:


print("abcdef".find("cd"))


# In[45]:


print("ccdcddcd".find("c"))


# In[46]:


print("Hello {0} and {1}".format('foo', 'bin'))


# In[47]:


print("Hello {1} and {0}".format('bin', 'foo'))


# In[48]:


print("Hello {} and {}".format('foo', 'bin'))


# In[77]:


print("Hello {name1} and {name2} ".format('foo', 'bin'))


# In[76]:


print("Hello {name1} and {name2} ".format(name1='foo',name2='bin'))


# In[51]:


print('The sum of {0} and {1} is {2}'.format(2, 10, 12))


# In[52]:


print('ab12'.isalnum())


# In[53]:


print('ab,12'.isalnum())


# In[54]:


print('ab'.isalpha())


# In[55]:


print('a B'.isalpha())


# In[56]:


print('0xa'.isdigit())


# In[57]:


print(''.isdigit())


# In[58]:


print('my_string'.isidentifier())


# In[59]:


print('$my_string'.isidentifier())


# In[60]:


print('abc'.islower())


# In[61]:


print('a@ 1,'.islower())


# In[62]:


print('11'.isnumeric())


# In[63]:


print('HelloWorld'.istitle())


# In[64]:


print('Hello World'.istitle())


# In[65]:


s1=''' hello
hi
how are you'''
print(s1)


# In[66]:


s1=''' hello
hi
how are you'''
print(s1.strip())


# In[67]:


print('abcdef'.partition('cd'))


# In[68]:


print('abcdefcdgh'.partition('cd'))


# In[69]:


print('abcd'.partition('cd'))


# In[70]:


print('abcdef12'.replace('cd', '12'))


# In[71]:


print('abef'.replace('cd', '12'))


# In[72]:


print('abcdefcdghcd'.split('cd'))


# In[74]:


print('Ab!2'.swapcase())


# In[78]:


print('ab cd ef'.title())


# In[79]:


print('ab cd-ef'.title())


# In[ ]:




