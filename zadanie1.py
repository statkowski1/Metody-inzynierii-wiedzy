#!/usr/bin/env python
# coding: utf-8

# In[15]:


import numpy as np
#zadanie 1
vector = np.array([1, 4, 5, 6, 2, 1, 5, 6, 7, 0])
print(vector)


# In[16]:


vector2 = np.delete(vector, 5)
print(vector2)


# In[17]:


vector3 = np.insert(vector, 10, 8)
print(vector3)


# In[18]:


vector4 = np.zeros(10)
for i in range(0, vector.shape[0]):
    if i%2==1:
        vector4[i] = vector[i] * 2
    else:
        vector4[i] = vector[i]
print(vector4)


# In[31]:


vector5 = vector[::-1]
print(vector5)


# In[29]:


#zadanie 2
#mnożenie przez skalar
vec = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
skalar = 5
result = vec * skalar
print("Skalar mnoży każdą liczbę listy")
print(result)
#mnożenie dwóch list
vec2 = np.array([0, 2, 4, 6, 8, 10, 12, 14, 16])
result2 = vec * vec2
print("W dwóch listach liczby na tych saych indeksach mnożą się ze sobą")
print(result2)


# In[20]:


#zadanie 3
x = np.array([3, 5, 0, 2, 6, 1, 3, 8, 9]).reshape(3, 3)
x[0][0] = -2
x[1][1] = 44
x[-1][-1] = 0
x


# In[21]:


#zadanie 4
for i in range(0, x.shape[0]):
    for j in range(0, x.shape[1]):
        if i%2==0 and j%2==0:
            x[i][j] = 0
x


# In[23]:


#zadanie 5
a = np.array([2, 1, 1, 1, 3, 6, 4, 5, 5]).reshape(3, 3)
b = np.array([1, 0, 5, 2, 1, 6, 0, 3, 0]).reshape(3, 3)
c = np.zeros((3, 3))
for i in range(0, a.shape[0]):
    for j in range(0, a.shape[1]):
        c[i][j] = a[i][j] + b[i][j]
c


# In[25]:


get_ipython().run_line_magic('pip', 'install tensorflow')


# In[26]:


#zadanie 6
import tensorflow as tf
tensor = tf.constant([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
print(tensor)


# In[32]:


#dim=2 (wymiar), rozmiar: 4x4, wartość typ: int


# In[ ]:




