#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("Hello world")


# #Heading

# In[5]:


x = 4
print(type(x))


# In[7]:


import keyword


# In[8]:


keyword.kwlist


# In[9]:


var=5


# In[14]:


a = int(input("Enter a value "))


# In[15]:


type(a)


# In[7]:


s = int(input("Enter the side of the square "))
area = s*s
print(area)


# In[10]:


h = int(input("Enter the height of the traingle "))
b = int(input("Enter the base of the traingle "))
area = (b*h)/1/2
print(area)


# In[14]:


p = int(input("Enter the Principal "))
r = int(input("Enter the rate of interest "))
t = int(input("Enter the time "))
si = (p*r*t)/100
print(si)


# In[19]:


p = int(input("Enter the Principal "))
r = int(input("Enter the rate of interest "))
n = int(input("Enter the time "))
ci = p(1 + (r/100))^n
print(ci)


# In[21]:


p = float(input("Enter the purchase price "))
s = float(input("Enter the selling price "))
profit = s - p
print("You have made profit of ", profit)


# In[22]:


p = float(input("Enter the purchase price "))
s = float(input("Enter the selling price "))
loss = p - s
print("You have made loss of ", loss)


# In[ ]:


p = float(input("Enter the purchase price "))
s = float(input("Enter the selling price "))
if s>p:
    pf = s-p
    p_p = pf/p*100
    print("You have made profit of ", pf)
    print("You have made profit % of ", p_p)
elif p == s:
    print("No profit No loss ")
else:
    p>s
    l = p-s
    l_p = l/p*100
    print("You have made loss of ", l)
    print("You have made loss % of ", l_p)


# In[23]:


n = int(input("Enter the number"))
if n%2==0:
    print("number is even")
else:
    print("Number is odd")


# In[25]:


n  = int(input("Enter the number"))
if n>0:
    print("Number is positive")
else:
    print("number is negative")


# In[40]:


salary = int(input("Enter your salary "))
if salary>500000>100000:
    incometax = salary*0.10
    print("You have to pay income tax of rupees", incometax)
    if salary>100000>1500000:
        incometax = salary*0.15
        print("You have to pay income tax of rupees", incometax)
        if salary>1500000:
            incometax = salary*0.20
            print("You have to pay income tax of rupees", incometax)
else:
    print("Youuu are out of the income tax slab")


# In[46]:


Budget = int(input("Enter your budget"))
if Budget>20000>30000:
    print("Your destination will be Shimla",Budget)


# In[ ]:




