#!/usr/bin/env python
# coding: utf-8

# In[3]:


class UserData():
    age = 0
    name = None
    def __init__(self, name, age):
        self.name = name
        self.age  = age
    def user(self):
        print('User name is: {} and has {} years old.'.format(self.name,self.age))
user_1 = UserData('Sara', 40)


# In[4]:


print(user_1.name)


# In[5]:


type(user_1)


# In[6]:


user_2 = UserData('David', 50)


# In[7]:


print(user_2.age)


# In[8]:


user_3 = UserData('John', 30)
user_4 = UserData('Peter', 15)


# In[9]:


avg_age = (user_1.age + user_2.age + user_3.age + user_4.age)/3
print(avg_age)


# In[10]:


user_1.user()


# In[17]:


class Rectangle():
    def __init__(self, length, width):
        self.width = width
        self.length = length
    def rect_area(self):
        return(self.length*self.width)
rect_1 = Rectangle(50,30)
rect_2 = Rectangle(140,60)
rect_3 = Rectangle(120,70)
rect_4 = Rectangle(100,80)


# In[18]:


rect_1.length


# In[19]:


rect_2.width


# In[24]:


rect_3.rect_area()


# In[21]:


type(rect_4)


# In[23]:


print((rect_1.rect_area()+rect_2.rect_area()+rect_3.rect_area()+rect_2.rect_area())/4)


# In[ ]:



#create  fruits Class has the following three properties:-name-kind-color

class Fruta():
    def __init__(self,nombre, tipo, color,cantidad):
        self.nombre = nombre
        self.tipo = tipo
        self.color = color
        self.cantidad = cantidad

    def __str__(self):
        return (self.nombre)

    def __len__(self):
        return self.cantidad

    

manzana = Fruta("Manzana","Arbol","roja",12)
banana = Fruta("Banana","Arbol","Amarilla",12)
uva = Fruta("Uva","Ramo","Morada",13)

frutas = [manzana, banana]

for i in frutas:

    if(i.tipo == "Arbol"):
        print(i.nombre)




#Given a class for a BasicPlan, write the classes for StandardPlan and PremiumPlan which have class attributes of the following:

class BasicPlan():
    price = "$8.99"
    canStream = True
    canDownload = True
    hasHD = False
    SDorHD = True
    numDevices = 1

    def __init__(self):
        super().__init__()

class StandardPan(BasicPlan):
    price = "$12.99"
    numDevices = 2
    hasHD = True

class PremiumPlan(StandardPan):
    numDevices = 4
    price = "$15.99"
    hasUHD = True



#Use Subclass(Parentclass) to define a child classes of gender.

class Persona():

    def Genero(self):
        print("Desconocido")


class Hombre(Persona):

    def getGenero(self):
        print("Hombre")

class Mujer(Persona):

    def getGenero(self):
        print("Mujer")



maria = Mujer()

maria.getGenero()

mario = Hombre()

mario.getGenero()




    


