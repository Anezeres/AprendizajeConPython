#!/usr/bin/env python
# coding: utf-8

# In[2]:


class DataUser():
    def __init__(self, name, age):
        self.name = name
        self.age= age
        
    def __str__(self):
        return' User name is: {} and has {} years old.'.format(self.name, self.age)
    
    def __len__(self):
        return self.age

user_1 = DataUser('Mostafa', 16)
user_2 = DataUser('Tamer', 36)
     


# In[3]:


print(user_1)


# In[4]:


str(user_1)


# In[5]:


len(user_1)


# In[7]:


str(user_1)


# In[6]:


len(user_2)


# In[ ]:




