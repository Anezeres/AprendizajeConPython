#!/usr/bin/env python
# coding: utf-8

# In[ ]:


user_name_and_car_color  = {'David':'red','John':'green','Sara':'yellow'}


# In[ ]:


user_name_and_car_color['Kate'] = 'black'
print(user_name_and_car_color)


# In[ ]:


#In order to remove the item with key = “Kate” and print dictionary:
del user_name_and_car_color['Kate']


# In[ ]:


#In order to print the item with key = “David” code as following:
print(user_name_and_car_color['David'])


# In[ ]:


print(user_name_and_car_color['Sara'])      


# In[ ]:


print(user_name_and_car_color['John'])      


# In[ ]:


user_name_and_car_color.get('John')    


# In[ ]:


'David' in user_name_and_car_color


# In[ ]:


'Kate' in user_name_and_car_color


# In[ ]:


'red'in user_name_and_car_color.values()


# In[ ]:


'black'in user_name_and_car_color.values()


# In[ ]:


user_name_and_car_color.clear()


# In[ ]:


print(user_name_and_car_color)


# In[ ]:


user_name_and_car_color  = {'David':'red','John':'green','Sara':'yellow'}
user_name_and_car_color.pop('John')


# In[ ]:


user_name_and_car_color  = {'David':'red','John':'green','Sara':'yellow'}
user_name_and_car_color.items()


# In[ ]:


#Write a python code to arrange the following dictionary 
values = {'key_1': [20, 80, 50], 'key_2': [200, 10, 100], 'key_3': [300, 20, 400]}

arregloNumeros = []
arregloValues = []
arregloFinal = []

for i in values.values():
    for y in i:
        arregloNumeros.append(y)

arregloNumeros.sort()

print(arregloNumeros)

arregloValues = []

contadorPosicion = -1

for i in arregloNumeros:

    arregloFinal.append(i)

    if(len(arregloFinal) == 3):
        arregloValues.append(arregloFinal)

        for i, j in zip(arregloFinal, values.keys()):

                values.update({j:i})

        arregloFinal = []


print(values)

print(arregloValues)





