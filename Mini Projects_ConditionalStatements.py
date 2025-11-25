#!/usr/bin/env python
# coding: utf-8

# In[4]:


item_name = input("Enter item name: ")
price = float(input("Enter price of the item: "))
qty = int(input("Enter quantity: "))
if qty <= 0:
    print("Invalid quantity! Please enter a positive value.")
    subtotal = 0
else:
    subtotal = price * qty
    print("Subtotal:", subtotal)
if qty > 10:
    quantity_discount = subtotal * 0.50
else:
    quantity_discount = 0
print("Quantity Discount:", quantity_discount)

loyal = input("Is the customer loyal? (yes/no): ").lower()

total_after_quantity_discount = subtotal - quantity_discount
if loyal == "yes":
    loyal_discount = total_after_quantity_discount * 0.10
else:
    loyal_discount = 0

print("Loyalty Discount:", loyal_discount)
final_bill = total_after_quantity_discount - loyal_discount
print("Final Bill Amount:", final_bill)


# In[15]:


total = float(input("Enter total purchase amount: "))
payment = input("Enter payment mode (credit/debit/cash): ").lower()
if total < 100:
    discount = 0
elif total < 500:
    discount = 0.05 * total
elif total < 1000:
    discount = 0.10 * total
else:
    discount = 0.15 * total
fee = 0
cash_discount = 0

match payment:
    case 'credit':
        fee = 0.02 * total   
    case 'debit':
        fee = 0.01 * total   
    case 'cash':
        cash_discount = 5    
    case _:
        print("Invalid payment mode")
        quit()
        
final_amount = total - discount - cash_discount + fee

print("\n------ BILL SUMMARY ------")
print("Purchase Amount:", total)
print("Discount Applied:", discount)
print("Payment Mode:", payment)
print("Extra Fee:", fee)
print("Cash Discount:", cash_discount)
print("---------------------------")
print("Final Amount to Pay:", final_amount)


# In[1]:


is_delivery=input("Is deliver required? (y/n):")
is_premium=input("Is customer is a premium member? (y/n):")
Total=eval(input("Enter total value:"))
if is_delivery:
    if Total>500:
        print("Delivery Fee is: 0")
    else:
        print("Delivery Fee is 50")
else:
    print("No delivery Delivery Fee is: 0")
if is_premium:
    if Total>200:
        delivery_fee=0
        print("Free delivery for large orders",delivery_fee)
    else:
        deliver_fee=50
        print("Delivery Fee is 50")
else:
    print("Delivery Fee is 0 if not delivered")
if is_premium:
    if Total>200:
        Bonus_points=50
        print("Bonus_points:",Bonus_points)
    else:
        Bonus_points=10
        print("Bonus_points:",Bonus_points)
else:
    Normal_Points=5
    print("Normal_points:",Normal_Points)


# In[19]:


subtotal=int(input("enter subtotal:"))
ch=input("enter choice(essential/luxury goods/electronics):")
match ch:
    case 'essential':
        tax=subtotal*0.05
        total=subtotal+tax
        print("total price of product is:",total)
    case 'luxury goods':
        tax=subtotal*0.20
        total=subtotal+tax
        print("total price of product is:",total)
    case 'electronics':
        tax=subtotal*0.12
        total=subtotal+tax
        print("total price of product is:",total)


# In[ ]:




