#!/usr/bin/env python
# coding: utf-8

# In[1]:


my_list =[1,4,20,50,100,2000,10000,6]
sum(my_list)


# In[24]:


max(my_list)


# In[25]:


min(my_list)


# In[26]:


len(my_list)


# In[ ]:


#Write  Python code lines to get the sum all numbers
#  in a list then get the result of multiplying them,
#  then get the largest number of them, then get the smallest number 
# of them, finally get the numbers of items in that list.

lista = [12,13,15,14,18,1561,123]

print(sum(lista))

multiplicacion = 1

for i in lista:
    multiplicacion *= i

print("Multiplicacion = ",multiplicacion)

print("Valor maximo = ",max(lista))
print("Valor minimo = ",min(lista))
print("Longitud del Array = ",len(lista))



# In[ ]:




