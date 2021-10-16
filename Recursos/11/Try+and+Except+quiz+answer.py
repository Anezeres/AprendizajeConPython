#!/usr/bin/env python
# coding: utf-8

# # Check if the python text file is exist by using (try & except statement)

# # Solution:

# In[10]:


#The try block of code will raise an error when trying to open non-existed python text file:

try:
  f = open("python.txt")
except:
  print("Something went wrong when try to open the file")
finally:
  f.close()

#The code continue, without leaving the file opened if the file is exis:


# In[ ]:




