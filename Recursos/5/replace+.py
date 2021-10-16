#!/usr/bin/env python
# coding: utf-8

# In[1]:


'This is user car'.replace('user', 'my')


# In[2]:


#In order to replace a character many times:
'This is user car'.replace('s', 'c', 3)


# In[ ]:

#then check the string case. then make it in upper case  in one code finally make it in lower case in a second code.

mensaje = "The coding is fun"

print(mensaje.replace("fun","awesome"))
print(mensaje.strip("The"))

print("----------")


mensaje = "HoLa Como estás, MuNdo"
print(mensaje.capitalize())
print(mensaje.title())
print(mensaje.swapcase())
print(mensaje.upper())
print(mensaje.lower())





