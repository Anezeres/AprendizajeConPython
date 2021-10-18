#!/usr/bin/env python
# coding: utf-8

# In[30]:


name = "Alexander"
car_color  = "red"
print("hello world, my name is"+" "+name+" "+",and my car color is"+" "+car_color)


# In[31]:


msg ="hello world, my name is {} , and my car color is {}".format(name, car_color)
print(msg)

print(len(name))
print(len(car_color))
print(len(msg))

lista = [0,1,2,3,4,5,6,7,8,9]

print(lista[1:5])


print("----------------")

mensaje = "No correr en este lugar     0000"

print(len(mensaje))
print(mensaje.count("o"))

print(mensaje.count(" ",1,3))
print(mensaje.count(" "))

print("----------------")

#Write a program in python to count to count the vowels in the following string: "are you working as a Python programmer?"


mensaje = " are you working as a Python programmer ?"

vocales = ["a","e","i","o","u"]

for i in vocales:
    print(mensaje.count(i))




