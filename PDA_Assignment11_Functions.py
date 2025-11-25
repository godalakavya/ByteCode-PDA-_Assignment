#!/usr/bin/env python
# coding: utf-8

# In[2]:


def display():
    print("welcome to function concept")
display()


# In[9]:


def display():
    print("welcome to function concept")
display()


# In[10]:


def display123():
    print("welcome to function concept")
display123()


# In[11]:


def display(a):
    print("welcome to function concept", a)
display(10)


# In[12]:


def display(a):
    print("welcome to function concept", a)
display(99.7)


# In[13]:


def display(a):
    print("welcome to function concept", a)
display("Daniel")


# In[14]:


def display(a):
    for i in a:
        print(i)
display("Daniel")


# In[15]:


def display(a):
    print("welcome to function concept", a)
display([10, 20, 30, 40])


# In[16]:


def display(a):
    print("welcome to function concept", a)
b = [10, 20, 30, 40]
display(b)


# In[17]:


def display(a):
    for i in a:
        print(i)
b = [10, 20, 30, 40]
display(b)


# In[18]:


def display(a):
    for i in a:
        print(i+2)
b = [10, 20, 30, 40]
display(b)


# In[19]:


def display(a):
    print("welcome to function concept", a)
b = [10, "Daniel", 33.5]
display(b)


# In[20]:


def display(a):
    for i in a:
        print(i)
b = [10, "Daniel", 33.5]
display(b)


# In[22]:


def display(a):
    for i in a:
            print(i+1)
b = [10, "Daniel", 33.5]
display(b)


# In[23]:


def display(a):
    print("welcome to function concept", a)
b = (10, 20, 30, 40)
display(b)


# In[24]:


def display(a):
    for i in a:
            print(i)
b = (10, 20, 30, 40)
display(b)


# In[25]:


def display(a):
    print("welcome to function concept", a)
b = {10, 20, 30, 40}
display(b)


# In[26]:


def display(a):
    for i in a:
        print(i)
b = {10, 20, 30, 40}
display(b)


# In[27]:


def display(a):
    print("welcome to function concept", a)
b = {"id": 101, "name": "Daniel"}
display(b)


# In[28]:


def display(a):
    for i in a:
        print(i)
b = {"id": 101, "name": "Daniel"}
display(b)


# In[29]:


def display(a):
    for i in a:
        print(i, a[i])
b = {"id": 101, "name": "Daniel"}
display(b)


# In[30]:


def m1():
    a = 33
    b = 200
    if b > a:
        print("b is greater than a")
m1()


# In[31]:


def m1(a, b):
    if b > a:
        print("b is greater than a")
m1(33, 200)


# In[32]:


def m1():
    a = 33
    b = 33
    if b > a:
        print("b is greater than a")
    elif a == b:
        print("a and b are equal")
m1()


# In[34]:


def m1(a, b):
    if b > a:
        print("b is greater than a")
    elif a == b:
        print("a and b are equal")
m1(33, 33)


# In[35]:


def m1():
    a = int(input('Enter first number : '))
    b = int(input('Enter second number : '))
    c = int(input('Enter third number : '))
    largest = 0
    if a > b and a > c:
        largest = a
    elif b > a and b > c:
        largest = b
    elif c > a and c > b:
        largest = c
    print(largest, "is the largest of three numbers.")
m1()


# In[36]:


def m1(p):
    result = max(p)
    print(result, "is the largest of three numbers.")
a = [10, 20, 30]
m1(a)


# In[37]:


def addition(numbers):
    total = 0
    for x in numbers:
        total = total + x
    return total
result = addition([8, 2, 3, 0, 7])
print(result)


# In[38]:


def multiply(numbers):
    total = 1
    for x in numbers:
        total = total * x
    return total
result = multiply([1, 2, 3, 4])
print(result)


# In[39]:


def test_range(n):
    if n in range(3, 9):
        print( "The value is within the range", n)
    else:
        print("The number is outside the given range.")
test_range(5)


# In[41]:


text = input("Enter a string:")
count1 = 0
count2 = 0
for i in text:
        if i.islower():
            count1 = count1+1
        elif i.isupper():
            count2 = count2+1
print("The number of lowercase characters is:", count1)
print("The number of uppercase characters is:", count2)


# In[42]:


def unique_list(p):
    x = []
    for a in p:
        if a not in x:
            x.append(a)
    return x
result = unique_list([1, 2, 3, 3, 3, 3, 4, 5])
print(result)


# In[43]:


def is_even_num(a):
    enum = []
    for i in a:
        if i % 2 == 0:
            enum.append(i)
    return enum
b = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = is_even_num(b)
print(result)


# In[44]:


def display():
    a = list()
    r = range(1, 10)
    for i in r:
        a.append(i**2)
    print(a)
display()


# In[45]:


def display():
    a = []
    r = range(1, 10)
    for i in r:
        a.append(i**2)
    print(a)
display()


# In[48]:


from time import sleep
def traffic(r):
        for i in r:
                sleep(2)
                print(i)
traffic(range(1, 11))


# In[49]:


def 123display():
    print("welcome to function concept")
123display()


# In[50]:


def display123():
    print("welcome to function concept")
display123()


# In[51]:


def display_one():
    print("welcome to function concept")
display_one()


# In[52]:


def testing(a, b):
    print("two parameterised function:", a, b)
testing(10, 20)


# In[53]:


def testing(a, a):
    print("two parameterised function:", a, a)
testing(10, 20)


# In[54]:


def wish():
    print("Hello")
    print("How are you")
    return 100
b = wish()
print(b)


# In[55]:


def wish():
    print("Hello")
    return 100
    print("How are you")
b = wish()
print(b)


# In[56]:


def wish():
    print("Hello")
    return 100
    return 111
b = wish()
print(b)


# In[57]:


def balance():
    print("My bank balance is: ")
    return 100
print(balance())


# In[58]:


def details():
    id = 101
    name = "Daniel"
    salary = 10000
    return id, name, salary
result = details()
print("all values:", result)


# In[59]:


def sub(x, y):
    print(x-y)
sub(20, 10, 30)


# In[60]:


def cart(product, price):
    print("Product is :" , product)
    print("cost is :" , price)
cart("bangles", 20000)


# In[61]:


def cart(product, price):
    print("Product is :" , product)
    print("cost is :" , price)
cart(product = "bangles", 20000)


# In[1]:


def cart(product, price):
    print("Product is :" , product)
    print("cost is :" , price)
cart("bangles", price = 20000)


# In[3]:


def cart(product, price):
    print("Product is :" , product)
    print("cost is :" , price)
cart(product = "bangles", price = 20000)


# In[4]:


def cart(product, price):
    print("Product is :" , product)
    print("cost is :" , price)
cart(prod = "bangles", price = 20000)


# In[5]:


def cart(product, price):
    print("Product is :" , product)
    print("cost is :" , price)
cart(product = "bangles", pri = 20000)


# In[6]:


def cart(product, price):
    print("Product is :" , product)
    print("cost is :" , price)
cart(prod = "bangles", pri = 20000)


# In[7]:


def cart(product, price = 40.0):
    print("Product is :" , product)
    print("cost is :" , price)
cart(product = "pen")


# In[8]:


def cart(product, price = 40.0):
    print("product is :", product)
    print("cost is :", price)
cart(product = "handbag", price = 10000)


# In[9]:


def cart(product = "handbag", price):
    print("product is :", product)
    print("cost is :", price)
cart(price = 10000)


# In[10]:


def m(x):
    print(x)
m(10)


# In[11]:


def m(x):
    print(x)
m(10, 20)


# In[12]:


def m(*x):
    print(x)
m(10)


# In[13]:


def m(*x):
    print(x)
m(10, 20)


# In[14]:


def m(*x):
    print(x)
m(10, 20, 30)


# In[15]:


def m(a, *x):
    print(a)
    print(x)
m(10, 20, 30)


# In[16]:


def m(*x, a):
    print(a)
    print(x)
m(10, 20, 30)


# In[17]:


def display(**kwargs):
    print(kwargs)
display(id = 1, name = "Daniel", qualification = "MCA")


# In[18]:


a = lambda b : b + 15
result = a(10)
print(result)
print(a(10))


# In[19]:


a = lambda b : b * 15
result = a(10)
print(result)
print(a(10))


# In[20]:


a = lambda x, y : x * y
result = a(10, 20)
print(result)
print(a(10, 20))


# In[21]:


def func_compute(n):
    return lambda x : x * n
result = func_compute(2)
print("Double the number of 15 =", result(15))
result = func_compute(3)
print("Triple the number of 15 =", result(15))
result = func_compute(4)
print("Quadruple the number of 15 =", result(15))
result = func_compute(5)
print("Quintuple the number 15 =", result(15))


# In[22]:


subject_marks = [('English', 88), ('Science', 90), ('Maths', 97),
('Social sciences', 82)]
print("Original list of tuples:")
print(subject_marks)
subject_marks.sort(key = lambda x: x[1])
print("Sorting the List of Tuples:")
print(subject_marks)


# In[23]:


models = [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make':
'Mi Max', 'model':'2', 'color': 'Gold'}, {'make': 'Samsung', 'model':
7, 'color': 'Blue'}]
print("Original list of dictionaries :")
print(models)
sorted_models = sorted(models, key = lambda x: x['color'])
print("Sorting the List of dictionaries :")
print(sorted_models)


# In[24]:


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Original list of integers:")
print(nums)
print("Even numbers from the said list:")
even_nums = list(filter(lambda x: x%2 == 0, nums))
print(even_nums)
print("Odd numbers from the said list:")
odd_nums = list(filter(lambda x: x%2 != 0, nums))
print(odd_nums)


# In[25]:


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Original list of integers:")
print(nums)
print("Square every number of the said list:")
square_nums = list(map(lambda x: x ** 2, nums))
print(square_nums)
print("Cube every number of the said list:")
cube_nums = list(map(lambda x: x ** 3, nums))
print(cube_nums)


# In[26]:


starts_with = lambda x: True if x.startswith('P') else False
print(starts_with('Python'))
print(starts_with('Java'))


# In[27]:


import datetime
now = datetime.datetime.now()
print(now)
year = lambda x: x.year
month = lambda x: x.month
day = lambda x: x.day
t = lambda x: x.time()
print(year(now))
print(month(now))
print(day(now))
print(t(now))


# In[28]:


array_nums1 = [1, 2, 3, 5, 7, 8, 9, 10]
array_nums2 = [1, 2, 4, 8, 9]
print("Original arrays:")
print(array_nums1)
print(array_nums2)
result = list(filter(lambda x: x in array_nums1, array_nums2))
print ("Intersection of the said arrays: ",result)


# In[29]:


array_nums = [-1, 2, -3, 5, 7, 8, 9, -10]
print("Original arrays:")
print(array_nums)
result = sorted(array_nums, key = lambda i: 0 if i == 0 else -1 / i)
print("Rearrange positive and negative numbers of the said
array:")
print(result)


# In[30]:


array_nums = [1, 2, 3, 5, 7, 8, 9, 10]
print("Original arrays:")
print(array_nums)
odd_ctr = len(list(filter(lambda x: (x%2 != 0) , array_nums)))
even_ctr = len(list(filter(lambda x: (x%2 == 0) , array_nums)))
print("Number of even numbers in the above array: ", even_ctr)
print("Number of odd numbers in the above array: ", odd_ctr)


# In[31]:


weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday',
'Friday', 'Saturday', 'Sunday']
days = filter(lambda day: day if len(day)==6 else '', weekdays)
for d in days:
    print(d)


# In[32]:


nums1 = [1, 2, 3]
nums2 = [4, 5, 6]
print("Original list:")
print(nums1)
print(nums2)
result = map(lambda x, y: x + y, nums1, nums2)
print("Result: after adding two list")
print(list(result))


# In[37]:


nums = [19, 65, 57, 39, 152, 639, 121, 44, 90, 190]
print("Orginal list:")
print(nums)
result = list(filter(lambda x: (x % 19 == 0 or x % 13 == 0), nums))
print("Numbers of the above list divisible by nineteen or
thirteen: ")
print(result)


# In[34]:


str1 = "sdf 23 safs8 5 sdfsd8 sdfs 56 21sfs 20 5"
str_num = [i for i in str1.split(' ')]
num_str = sorted([x for x in str_num if x.isdigit()])
numbers = sorted([int(x) for x in str_num if x.isdigit()])
print(str1)
print(str_num)
print(num_str)
print(numbers)


# In[35]:


nums = [2, 4, -6, -9, 11, -12, 14, -5, 17]
print("Original list:", nums)
total_negative_nums = list(filter(lambda nums: nums<0,nums))
total_positive_nums = list(filter(lambda nums: nums>0,nums))
t_n = sum(total_negative_nums)
t_p = sum(total_positive_nums)
print("Sum of the positive numbers: ", t_n)
print("Sum of the negative numbers: ", t_p)


# In[36]:


def m1(list1, list2):
    result = list(filter(lambda x: x not in list2, list1))
    return result
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = [2, 4, 6, 8]
print(m1(a, b))


# In[38]:


def m2(p):
    result = list(map(lambda x: "".join(reversed(x)), p))
    return result
a = ["Red", "Green", "Blue", "White", "Black"]
b = m2(a)
print(b)


# In[39]:


def count_occurrences(nums):
    result = dict(map(lambda el : (el, list(nums).count(el)),
    nums))
    return result
nums = [3, 4, 5, 8, 0, 3, 8, 5, 0, 3, 1, 5, 2, 3, 4, 2]
print(nums)
print(count_occurrences(nums))


# In[40]:


def remove_words(list1, r_words):
    result = list(filter(lambda word: word not in r_words,
    list1))
    return result
colors = ['orange', 'red', 'green', 'blue', 'white', 'black']
remove_colors = ['orange', 'black']
print(colors)
print(remove_colors)
print(remove_words(colors, remove_colors))


# In[ ]:




