#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("Twinkle, twinkle, little star,\n\t How I wonder what you are!\n\t\t Up above the world so high,\n\t\t Like a diamond in the sky. Twinkle, twinkle, little star,\n\t How I wonder what you are")


# In[3]:


import sys
print(sys.version)


# In[5]:


from datetime import datetime
print(datetime.now())


# In[9]:


radius = 1.1
Area = 2*3.14*radius
print("Area of circle", Area )


# In[14]:


def reverse(Firstname):
    str = ""
    for i in Firstname:
        str = i + str
    return str
Firstname = "SachinGupta"
print(reverse(Firstname))


# In[16]:


Fname = input("Input your First name")
Lname = input("Input your Last name")
print(Lname + " " + Fname)


# In[16]:


x = int(input())
y = int(input())
if x>10 and x<=500 and y>50 and y<200:
    print(x+y)
    print(x-y)
    print(x*y)


# In[19]:


n= int(input())
if n>1 and n<=200:
    for i in range(n):
        print(i*i)


# In[32]:


year = int(input())
if year%4==0 and year%100!=0:
    print("its leap year")
elif year%100==0 and year%400==0:
    print("its a leap year")
else:
    print("not a leap year")
    


# In[34]:


a =int(input())
for i in range(a):
    print(i+1)


# In[2]:


a = input(" first")
b = input("last")
print("Hello"+" "+a+" "+b+" 1 you fucked")


# In[5]:


import pandas as pd
import numpy as np
titanic = pd.read_csv("train.csv")
print(titanic.head())


# In[7]:


name = input()
print("Hello"+" "+name)


# In[12]:


length = int(input())
width = int(input())
area = length*width
accer = area/43560
print(accer, "accer")


# In[13]:


one= int(input())
more = int(input())
x = one*.10
y = more*.25
z = (x+y)/60
print("$", z)


# In[7]:


meal = int(input())
tax = .2
tip = .18
total = meal+(tax*meal+tip*meal)
print("%.2f" %total)


# In[10]:


a = int(input())
sum = (a*a+a)/2
print(sum)


# In[15]:


a= int(input())
b= int(input())
c = 75
d = 112
total = a*75+b*112
print("total order weight", total, "gram")


# In[2]:


# input comma separated elements as string 
str = input("Enter comma separated integers: ")
list = str.split(",")
tuple = tuple(list)
print(tuple)
print(list)


# In[ ]:


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
arr.sort(reverse = True)
for i in range(n):
    if arr[i]==arr[i+1]:
          continue
    else:
        print(arr[i+1])
        break


# In[2]:


if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
print([ [ i, j, k] for i in range( x + 1) for j in range( y + 1) for k in range( z + 1) if ( ( i + j + k ) != n )])


# In[15]:


if __name__ == '__main__':
    N = int(input())
    nest = []
    for _ in range(N):
        name = input()
        score = float(input())
        nest.append([name,score])
    nest = sorted(nest, key=lambda x: x[1])
    print(nest[1][1])
    
    


# In[8]:


import datetime
d = datetime.date(2018,7, 27)
print(d)
today = datetime.date.today()
today7 = datetime.timedelta(days=8)
print(today + today7)
print(today.isoweekday())


# In[10]:


t = datetime.time(9,45,45,3)
print(t)


# In[12]:


import numpy as np
import pandas as pd
import h5py
d1 = np.random.random(size = (1000,1000))
d2 = np.random.random(size = (10000,100))
hf = h5py.File('E:\tcs qu\data.h5', 'w')
hf.create_dataset('dataset_1', data=d1)
hf.create_dataset('dataset_2', data=d2)
hf.close()


# In[ ]:





# In[ ]:




