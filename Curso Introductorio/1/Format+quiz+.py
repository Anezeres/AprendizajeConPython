#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Write a program in python that take two string to complete and form a message that we can understand
#the message is "python is               &                 language":

parte1 = "beautiful"
parte2 = "i love the"

mensaje1 = "python is",parte1,"&",parte2,"language"

mensaje2 = "python is"+parte1+"&"+parte2+"language"

mensaje3 = "python is {} & {} language".format(parte1,parte2)

print(type(mensaje1))
print(type(mensaje2))
print(type(mensaje3))

print(mensaje1)
print (mensaje2)
print(mensaje3)

print(len(mensaje1))
print(len(mensaje2))
print(len(mensaje3))

