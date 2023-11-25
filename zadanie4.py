#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np

#zadanie 1
def rownania_liniowe(arg):
    if arg.shape[0]==2 and arg.shape[1]==3:
        D = arg[0][0]*arg[1][1] - arg[0][1]*arg[1][0]
        Dx = arg[0][2]*arg[1][1] - arg[0][1]*arg[1][2]
        Dy = arg[0][0]*arg[1][2] - arg[0][2]*arg[1][0]
        x = Dx/D
        y = Dy/D
        return x, y
    elif arg.shape[0]==3 and arg.shape[1]==4:
        D = arg[0][0]*arg[1][1]*arg[2][2] + arg[0][1]*arg[1][2]*arg[2][0] + arg[0][2]*arg[1][0]*arg[2][1] - arg[0][2]*arg[1][1]*arg[2][0] - arg[1][2]*arg[2][1]*arg[0][0] - arg[2][2]*arg[0][1]*arg[1][0]
        Dx = arg[0][3]*arg[1][1]*arg[2][2] + arg[0][1]*arg[1][2]*arg[2][3] + arg[0][2]*arg[1][3]*arg[2][1] - arg[0][2]*arg[1][1]*arg[2][3] - arg[1][2]*arg[2][1]*arg[0][3] - arg[2][2]*arg[0][1]*arg[1][3]
        Dy = arg[0][0]*arg[1][3]*arg[2][2] + arg[0][3]*arg[1][2]*arg[2][0] + arg[0][2]*arg[1][0]*arg[2][3] - arg[0][2]*arg[1][3]*arg[2][0] - arg[1][2]*arg[2][3]*arg[0][0] - arg[2][2]*arg[0][3]*arg[1][0]
        Dz = arg[0][0]*arg[1][1]*arg[2][3] + arg[0][1]*arg[1][3]*arg[2][0] + arg[0][3]*arg[1][0]*arg[2][1] - arg[0][3]*arg[1][1]*arg[2][0] - arg[1][3]*arg[2][1]*arg[0][0] - arg[2][3]*arg[0][1]*arg[1][0]
        x = Dx/D
        y = Dy/D
        z = Dz/D
        return x, y, z
    else:
        return "Błąd! Została podana nieprawidłowa ilość danych!"
    
a = np.array([[3, 5, -7], [1, 4, -14]])
b = np.array([[1, 2, 3, -5], [3, 1, -3, 4], [-3, 4, 7, -7]])

print(rownania_liniowe(a))
print(rownania_liniowe(b))


# In[ ]:




