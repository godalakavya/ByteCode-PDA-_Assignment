#!/usr/bin/env python
# coding: utf-8

# In[2]:


password='admin123'
user_password=input("enter password:")
if user_password==password:
    print("correct password")
else:
    print("incorrect password")


# In[3]:


age=int(input("enter age:"))
if age>=18:
    print("A-rated movie")
else:
    print("not eligible")


# In[4]:


offer=int(input("enter Recharge offer:"))
if offer>=199:
    print("free 2GB data coupon")
else:
    print("No coupon applicable")


# In[5]:


marks=int(input("enter marks:"))
if marks>=90:
    print("Grade: A","Excellent")
elif marks>=70:
    print("Grade :B","good")
else:
    print("Grade: F","Failed")


# In[6]:


temp=int(input("enter temperature:"))
if temp>20:
    print("Its too sunny")
else:
    print("Its cold")


# In[7]:


Cibil=700
salary=30000
emp_salary=int(input("enter Employee Salary:"))
if emp_salary>=30000:
    emp_cibil=int(input("enter Employee cibil Score:"))
    if emp_cibil>=700:
        print("Eligible for credit card")
    else:
        print("insufficient cibil score")
else:
    print("ur Not Eligible due to Insufficient salary")


# In[8]:


balance=50000
withdraw=int(input("Enter Amount"))
if withdraw<=balance:
    if(balance%10==0):
        print("Transaction Succesful...")
    else:
        print("enter balance in multiple of 100")
else:
    print("Insufficient Balnace")


# In[9]:


number=int(input("enter mobile number:"))
mobileno=str(number)
if len(mobileno)==10:
    if mobileno[0]=='6':
        print("mobile Number is validate")
    elif mobileno[0]=='7':
        print("mobile Number is validate")
    elif mobileno[0]=='8':
        print("mobile Number is validate")
    elif mobileno[0]=='9':
        print("mobile Number is validate")
    else:
        print("number starts with 6/7/8/9")
else:
    print("enter 10 digits mobile number")


# In[10]:


units = int(input("Enter units consumed: "))
ch = input("Enter choice (home/shop/industry): ")
match ch:
    case "home":
        bill=units*5  
        print("Category: Domestic",bill)
    case "shop":
        bill=units*8       
        print("Category: Commercial",bill)
    case "industry":
        bill=units*10       
        print("Category: Industrial",bill)
    case _:
        print("Invalid connection type!")
        


# In[11]:


num1=eval(input("enter first number:"))
num2=eval(input("enter second number:"))
ch=input("enter operator(+,-,*,/):")
match(ch):
    case'+':
        print(f' {num1}+{num2} is: {num1+num2}')
    case '-':
        print(f' {num1}-{num2} is: {num1-num2}')
    case '*':
        print(f' {num1}*{num2} is: {num1*num2}')
    case '/':
        print(f' {num1}/{num2} is:{num1/num2}')
    case _:
        print("Invalid operator")
              


# In[ ]:




