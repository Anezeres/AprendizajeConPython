#!/usr/bin/env python
# coding: utf-8

# In[10]:


def rectangle_area(width, length):
           area = width * length 
           return area
rectangle_area(6, 9)


# In[9]:


rectangle_area(4, 15)


# In[4]:


def is_even(x):
    if x % 2 == 0:
        return True
    else:       
        return False


# In[5]:


is_even(10)


# In[13]:


def is_odd(y):
    if y % 2 != 0:
        return True
    else:       
        return False 
is_odd(8)


# In[17]:


def countdown(x):
    while x> 0:
        print(x)
        x = x-1
        print("Stop this is the end!")
        
countdown(2)


# In[20]:


def is_even_or_odd(x):
    if x % 2 == 0:
        return "this number is even"
    else:
        return "this number is odd"
is_even_or_odd(2)


# In[21]:


is_even_or_odd(7)


# In[ ]:


#create a python function that return maximum number of the following numbers:
lista = [2000,10000,500000,1000000,20000000]

def numeroMayor(list):

    mayor = max(list)
    
    return mayor

print(numeroMayor(lista))

#Create a lambda function that takes one parameter (a) and returns if it is even number or not:

texto = int(input("Escriba algo"))

y = lambda a : a

if (type(y(texto)) == str):
    print("Es una cadena de texto")

else:
    print("Es un numero")



