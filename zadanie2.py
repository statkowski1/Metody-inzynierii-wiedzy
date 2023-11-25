#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np

#zadanie 1
def mnozenie_macierzy(macierz_A, macierz_B):
    if macierz_A.shape[1] != macierz_B.shape[0]: #sprawdzam warunkiem czy macierze mają odpowiednie wymiary
        return "Błąd w mnożeniu macierzy! Macierze nie mają odpowiednich wymiarów, aby można byłoby je pomnożyć!"
    else:
        macierz_C = np.zeros((macierz_A.shape[0], macierz_B.shape[1])) #deklaruje macierz wypełnioną zerami, która ma przechować wyniki mnożenia
        
        #pętla która odpowiada za obliczenie wyniku mnożenia dwóch macierzy
        for i in range(0, macierz_C.shape[0]):
            for j in range(0, macierz_C.shape[1]):
                for k in range(0, macierz_A.shape[1]):
                    macierz_C[i][j] += macierz_A[i][k] * macierz_B[k][j]
        return macierz_C
    
A = np.array([[2, 1, 1], [1, 3, 6], [4, 5, 5]])
B = np.array([[1, 0, 5], [2, 1, 6], [0, 3, 0]])
print(mnozenie_macierzy(A, B))


# In[3]:


#zadanie 2
def wyznacznik_macierzy_3x3(macierz):
    if macierz.shape[0] != 3 and macierz.shape[1] != 3: #sprawdzam czy macierz ma odpowiednie wymiary
        return "Błąd! Macierz nie ma wymiarów 3x3!"
    else:
        #zwracam wyznacznik macierzy jako działanie stosując motodę Sarrusa
        return macierz[0][0]*macierz[1][1]*macierz[2][2] + macierz[0][1]*macierz[1][2]*macierz[2][0] + macierz[0][2]*macierz[1][0]*macierz[2][1] - macierz[0][2]*macierz[1][1]*macierz[2][0] - macierz[1][2]*macierz[2][1]*macierz[0][0] - macierz[2][2]*macierz[0][1]*macierz[1][0]

x = np.array([[1, 4, 5], [2, 1, 6], [0, 3, 2]])
print(wyznacznik_macierzy_3x3(x))


# In[4]:


#zadanie 3
def transponowanie_macierzy(macierz):
    wynik = np.zeros((macierz.shape[1], macierz.shape[0])) #wypełniam zerami pustą tablicę zamieniając odwrotnie rozmiar wierszy i kolumn
    
    #pętla która przypisuje liczby tak aby stworzyć transponowaną macierz
    for i in range(0, wynik.shape[0]):
        for j in range(0, wynik.shape[1]):
            wynik[i][j] = macierz[j][i]
    return wynik

t = np.array([[3, 2, 4, 1, 8, 0], [2, 3, 5, 6, 0, 3], [7, 7, 2, 1, 4, 5]])
print(transponowanie_macierzy(t))


# In[ ]:




