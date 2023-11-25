#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
np.set_printoptions(suppress=True)

def macierz_odwrotna(macierz):
    if macierz.shape[0]!=macierz.shape[1] and macierz.shape[0]<=3 and macierz.shape[1]<=3:
        return "Dana macierz nie jest kwadratowa lub jej wymiary nie są większe niż 3x3! Podaj prawidłowe dane!"
    else:
        macierz_jednostkowa = np.eye(macierz.shape[0], macierz.shape[1])
        copy = np.zeros((macierz.shape[0], macierz.shape[1]))
        for i in range(0, macierz.shape[0]):
            for j in range(0, macierz.shape[1]):
                copy[i][j] = macierz[i][j]
        for i in range(0, macierz.shape[0]):
            tmp = copy[i][i]
            for l in range(0, macierz.shape[0]):
                copy[i][l] = copy[i][l]/tmp
                macierz_jednostkowa[i][l] = macierz_jednostkowa[i][l]/tmp
            for j in range(0, macierz.shape[0]):
                if j!=i:
                    tmp = copy[j][i]
                    for k in range(0, macierz.shape[1]):
                        copy[j][k] = copy[j][k] - tmp * copy[i][k]
                        macierz_jednostkowa[j][k] = macierz_jednostkowa[j][k] - tmp * macierz_jednostkowa[i][k]
        return macierz_jednostkowa, copy


# In[2]:


matrix = np.array([[8, 1, 4, 2, 1], [8, 6, 4, 2, 1], [1, 2, 3, 4, 1], [8, 0, 6, 2, 5], [1, 9, 6, 4, 1]])
print(macierz_odwrotna(matrix)[0])
print(np.linalg.inv(matrix))
print(macierz_odwrotna(matrix)[1])
matrix2 = np.array([[5, 4, 3, 2, 1], [4, 3, 2, 1, 5], [3, 2, 9, 5, 4], [2, 1, 5, 4, 3], [1, 2, 3, 4, 5]])
print(macierz_odwrotna(matrix2)[0])
print(np.linalg.inv(matrix2))
print(macierz_odwrotna(matrix2)[1])


# 
