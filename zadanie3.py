#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np

#zadanie 1
def macierz_odwrotna_2x2(macierz):
    if macierz.shape[0]!=2 and macierz.shape[1]!=2: #sprawdzam czy macierz ma wymiary 2x2
        return "Błąd! Macierz nie ma wymiarów 2x2!" #zwracam komunikat o nieodpowiednich wymiarach macierzy
    else:
        det = macierz[0][0]*macierz[1][1] - macierz[0][1]*macierz[1][0] #obliczam wyznacznik macierzy
        if det==0: #jeśli wyznanik wynosi 0 zwracam komunikat o niemożliwości odwrócenia macierzy
            return "Wyznacznik wynosi zero, więc nie da się obliczyć macierzy odwrotnej!"
        else: #jeśli możliwe jest obliczenie macierzy to jest ona obliczana tzn. przeszła przez poprzednie warunki
            macierz_odwrotna = np.zeros((2, 2)) #deklaruje pustą tablicę 2x2
            #obliczam macierz odwrotną
            macierz_odwrotna[0][0] = macierz[1][1]
            macierz_odwrotna[0][1] = -macierz[0][1]
            macierz_odwrotna[1][0] = -macierz[1][0]
            macierz_odwrotna[1][1] = macierz[0][0]
            macierz_odwrotna = macierz_odwrotna/det
            return macierz_odwrotna


# In[2]:


A = np.array([[2, 1], [5, 3]])
print(macierz_odwrotna_2x2(A))


# In[3]:


print(np.linalg.inv(A))


# In[4]:


B = np.array([[-3, -9], [1, 3]])
print(macierz_odwrotna_2x2(B))


# In[5]:


print(np.linalg.inv(B))


# In[6]:


#zadanie 2
def macierz_odwrotna_3x3(macierz):
    if macierz.shape[0]!=3 and macierz.shape[1]!=3: #sprawdzam czy macierz ma wymiary 3x3
        return "Błąd! Macierz nie ma wymiarów 3x3!" #zwracam komunikat o nieodpowiednich wymiarach macierzy
    else:
        #obliczam wyznacznik macierzy
        det = macierz[0][0]*macierz[1][1]*macierz[2][2] + macierz[1][0]*macierz[2][1]*macierz[0][2] + macierz[2][0]*macierz[0][1]*macierz[1][2] - macierz[0][0]*macierz[2][1]*macierz[1][2] - macierz[2][0]*macierz[1][1]*macierz[0][2] - macierz[1][0]*macierz[0][1]*macierz[2][2]
        if det==0: #jeśli wyznanik wynosi 0 zwracam komunikat o niemożliwości odwrócenia macierzy
            return "Wyznacznik wynosi zero, więc nie da się obliczyć macierzy odwrotnej!"
        else: #jeśli możliwe jest obliczenie macierzy to jest ona obliczana tzn. przeszła przez poprzednie warunki
            macierz_odwrotna = np.zeros((3, 3)) #deklaruje pustą tablicę 3x3
            #obliczam macierz odwrotną
            macierz_odwrotna[0][0] = macierz[1][1]*macierz[2][2] - macierz[1][2]*macierz[2][1]
            macierz_odwrotna[0][1] = macierz[0][2]*macierz[2][1] - macierz[0][1]*macierz[2][2]
            macierz_odwrotna[0][2] = macierz[0][1]*macierz[1][2] - macierz[0][2]*macierz[1][1]
            macierz_odwrotna[1][0] = macierz[1][2]*macierz[2][0] - macierz[1][0]*macierz[2][2]
            macierz_odwrotna[1][1] = macierz[0][0]*macierz[2][2] - macierz[0][2]*macierz[2][0]
            macierz_odwrotna[1][2] = macierz[0][2]*macierz[1][0] - macierz[0][0]*macierz[1][2]
            macierz_odwrotna[2][0] = macierz[1][0]*macierz[2][1] - macierz[1][1]*macierz[2][0]
            macierz_odwrotna[2][1] = macierz[0][1]*macierz[2][0] - macierz[0][0]*macierz[2][1]
            macierz_odwrotna[2][2] = macierz[0][0]*macierz[1][1] - macierz[0][1]*macierz[1][0]
            macierz_odwrotna = macierz_odwrotna/det
            return macierz_odwrotna


# In[7]:


C = np.array([[1, 0, 5], [2, 7, 6], [8, 3, 2]])
print(macierz_odwrotna_3x3(C))


# In[8]:


print(np.linalg.inv(C))


# In[9]:


D = np.array([[3, -1, 1], [5, 1, 4], [-1, 3, 2]])
print(macierz_odwrotna_3x3(D))


# In[10]:


print(np.linalg.inv(D))


# In[11]:


#zadanie 3
def macierz_odwrotna_2x2_lub_3x3(macierz):
    if (macierz.shape[0]!=2 or macierz.shape[1]!=2) and (macierz.shape[0]!=3 or macierz.shape[1]!=3): #sprawdzam czy macierz ma wymiary 2x2 lub 3x3
        return "Błąd! Macierz nie ma wymiarów 2x2 ani 3x3!" #zwracam komunikat o nieodpowiednich wymiarach macierzy
    else: #jeśli macierzy ma wymiary 2x2 lub 3x3 przechodzę do tego warunku
        if macierz.shape[0]==2: #jeśli macierz ma wymiary 2x2 to przechodzę do tego warunku
            det = macierz[0][0]*macierz[1][1] - macierz[0][1]*macierz[1][0] #obliczam wyznacznik macierzy
            if det==0: #jeśli wyznanik wynosi 0 zwracam komunikat o niemożliwości odwrócenia macierzy
                return "Wyznacznik wynosi zero, więc nie da się obliczyć macierzy odwrotnej!"
            else:
                macierz_odwrotna = np.zeros((2, 2)) #deklaruje pustą tablicę 2x2
                #obliczam macierz odwrotną
                macierz_odwrotna[0][0] = macierz[1][1]
                macierz_odwrotna[0][1] = -macierz[0][1]
                macierz_odwrotna[1][0] = -macierz[1][0]
                macierz_odwrotna[1][1] = macierz[0][0]
                macierz_odwrotna = macierz_odwrotna/det
                return macierz_odwrotna
        elif macierz.shape[0]==3:
            #obliczam wyznacznik macierzy
            det = macierz[0][0]*macierz[1][1]*macierz[2][2] + macierz[1][0]*macierz[2][1]*macierz[0][2] + macierz[2][0]*macierz[0][1]*macierz[1][2] - macierz[0][0]*macierz[2][1]*macierz[1][2] - macierz[2][0]*macierz[1][1]*macierz[0][2] - macierz[1][0]*macierz[0][1]*macierz[2][2]
            if det==0: #jeśli wyznanik wynosi 0 zwracam komunikat o niemożliwości odwrócenia macierzy
                return "Wyznacznik wynosi zero, więc nie da się obliczyć macierzy odwrotnej!"
            else:
                macierz_odwrotna = np.zeros((3, 3)) #deklaruje pustą tablicę 3x3
                #obliczam macierz odwrotną
                macierz_odwrotna[0][0] = macierz[1][1]*macierz[2][2] - macierz[1][2]*macierz[2][1]
                macierz_odwrotna[0][1] = macierz[0][2]*macierz[2][1] - macierz[0][1]*macierz[2][2]
                macierz_odwrotna[0][2] = macierz[0][1]*macierz[1][2] - macierz[0][2]*macierz[1][1]
                macierz_odwrotna[1][0] = macierz[1][2]*macierz[2][0] - macierz[1][0]*macierz[2][2]
                macierz_odwrotna[1][1] = macierz[0][0]*macierz[2][2] - macierz[0][2]*macierz[2][0]
                macierz_odwrotna[1][2] = macierz[0][2]*macierz[1][0] - macierz[0][0]*macierz[1][2]
                macierz_odwrotna[2][0] = macierz[1][0]*macierz[2][1] - macierz[1][1]*macierz[2][0]
                macierz_odwrotna[2][1] = macierz[0][1]*macierz[2][0] - macierz[0][0]*macierz[2][1]
                macierz_odwrotna[2][2] = macierz[0][0]*macierz[1][1] - macierz[0][1]*macierz[1][0]
                macierz_odwrotna = macierz_odwrotna/det
                return macierz_odwrotna


# In[12]:


print(macierz_odwrotna_2x2_lub_3x3(A))


# In[13]:


print(macierz_odwrotna_2x2_lub_3x3(B))


# In[14]:


print(macierz_odwrotna_2x2_lub_3x3(C))


# In[15]:


print(macierz_odwrotna_2x2_lub_3x3(D))


# In[ ]:




