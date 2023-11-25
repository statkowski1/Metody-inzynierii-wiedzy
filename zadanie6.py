#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np

def rzad_macierzy(macierz):
    if macierz.shape[0]!=macierz.shape[1] or macierz.shape[0]>4 or macierz.shape[1]>4:
        return "Macierz ma być kwadratowa i obejmuje rozmiar maksymalnie 4x4"
    elif macierz.shape[0]==2:
        #sprawdzam czy rząd wynosi 2
        det = macierz[0][0]*macierz[1][1] - macierz[0][1]*macierz[1][0]
        if det!=0:
            return 2
        else:
            #sprawdzam czy rząd wynosi 1
            for i in range(0, macierz.shape[0]):
                for j in range(0, macierz.shape[1]):
                    if macierz[i][j]!=0:
                        return 1
            #rząd wynosi 0
            return 0
    elif macierz.shape[0]==3:
        #sprawdzam czy rząd wynosi 3
        det = macierz[0][0]*macierz[1][1]*macierz[2][2] + macierz[1][0]*macierz[2][1]*macierz[0][2] + macierz[2][0]*macierz[0][1]*macierz[1][2] - macierz[0][0]*macierz[2][1]*macierz[1][2] - macierz[2][0]*macierz[1][1]*macierz[0][2] - macierz[1][0]*macierz[0][1]*macierz[2][2]
        if det!=0:
            return 3
        else:
            #sprawdzam czy rząd wynosi 2
            x = 0
            y = 0
            for i in range(0, 9):
                tmp = np.zeros((2, 2))
                p = 0
                l = 0
                for j in range(0, macierz.shape[0]):
                    for k in range(0, macierz.shape[1]):
                        if j!=x and k!=y:
                            tmp[p][l] = macierz[j][k]
                            l += 1
                        if l>1:
                            l = 0
                            p += 1
                det = tmp[0][0]*tmp[1][1] - tmp[0][1]*tmp[1][0]
                if det!=0:
                    return 2
                y += 1
                if y==3:
                    y = 0
                    x += 1
            #sprawdzam czy rząd wynosi 1
            for i in range(0, macierz.shape[0]):
                for j in range(0, macierz.shape[1]):
                    if macierz[i][j]!=0:
                        return 1
            #rząd wynosi 0
            return 0
    elif macierz.shape[0]==4:
        #sprawdzam czy rząd wynosi 4
        det = macierz[0][0]*macierz[1][1]*macierz[2][2]*macierz[3][3] + macierz[0][0]*macierz[1][2]*macierz[2][3]*macierz[3][1] + macierz[0][0]*macierz[1][3]*macierz[2][1]*macierz[3][2] + macierz[0][1]*macierz[1][0]*macierz[2][3]*macierz[3][2] + macierz[0][1]*macierz[1][2]*macierz[2][0]*macierz[3][3] + macierz[0][1]*macierz[1][3]*macierz[2][2]*macierz[3][0] + macierz[0][2]*macierz[1][0]*macierz[2][1]*macierz[3][3] + macierz[0][2]*macierz[1][1]*macierz[2][3]*macierz[3][0] + macierz[0][2]*macierz[1][3]*macierz[2][0]*macierz[3][1] + macierz[0][3]*macierz[1][0]*macierz[2][2]*macierz[3][1] + macierz[0][3]*macierz[1][1]*macierz[2][0]*macierz[3][2] + macierz[0][3]*macierz[1][2]*macierz[2][1]*macierz[3][0] - macierz[0][0]*macierz[1][1]*macierz[2][3]*macierz[3][2] - macierz[0][0]*macierz[1][2]*macierz[2][1]*macierz[3][3] - macierz[0][0]*macierz[1][3]*macierz[2][2]*macierz[3][1] - macierz[0][1]*macierz[1][0]*macierz[2][2]*macierz[3][3] - macierz[0][1]*macierz[1][2]*macierz[2][3]*macierz[3][0] - macierz[0][1]*macierz[1][3]*macierz[2][0]*macierz[3][2] - macierz[0][2]*macierz[1][0]*macierz[2][3]*macierz[3][1] - macierz[0][2]*macierz[1][1]*macierz[2][0]*macierz[3][3] - macierz[0][2]*macierz[1][3]*macierz[2][1]*macierz[3][0] - macierz[0][3]*macierz[1][0]*macierz[2][1]*macierz[3][2] - macierz[0][3]*macierz[1][1]*macierz[2][2]*macierz[3][0] - macierz[0][3]*macierz[1][2]*macierz[2][0]*macierz[3][1]
        if det!=0:
            return 4
        else:
            #sprawdzam czy rząd wynosi 3
            x = 0
            y = 0
            for i in range(0, 16):
                tmp = np.zeros((3, 3))
                p = 0
                l = 0
                for j in range(0, macierz.shape[0]):
                    for k in range(0, macierz.shape[1]):
                        if j!=x and k!=y:
                            tmp[p][l] = macierz[j][k]
                            l += 1
                        if l>2:
                            l = 0
                            p += 1
                det = tmp[0][0]*tmp[1][1]*tmp[2][2] + tmp[1][0]*tmp[2][1]*tmp[0][2] + tmp[2][0]*tmp[0][1]*tmp[1][2] - tmp[0][0]*tmp[2][1]*tmp[1][2] - tmp[2][0]*tmp[1][1]*tmp[0][2] - tmp[1][0]*tmp[0][1]*tmp[2][2]
                if det!=0:
                    return 3
                y += 1
                if y==4:
                    y = 0
                    x += 1
            #sprawdzam czy rząd wynosi 2
            x1 = 0
            x2 = 1
            y1 = 0
            y2 = 1
            for i in range(0, 36):
                tmp = np.zeros((2, 2))
                p = 0
                l = 0
                for j in range(0, macierz.shape[0]):
                    for k in range(0, macierz.shape[1]):
                        if j!=x1 and j!=x2 and k!=y1 and k!=y2:
                            tmp[p][l] = macierz[j][k]
                            #print("p = "+str(p)+" l = "+str(l)+" i = "+str(i)+" j = "+str(j)+" k = "+str(k)+" x1 = "+str(x1)+" x2 = "+str(x2)+" y1 = "+str(y1)+" y2 = "+str(y2))
                            l += 1
                        if l>1:
                            l = 0
                            p += 1
                #print("tmp = "+str(tmp))
                det = tmp[0][0]*tmp[1][1] - tmp[0][1]*tmp[1][0]
                if det!=0:
                    return 2
                z = 0
                if x2==3 and y1==2 and y2==3 and z==0:
                    x1 += 1
                    x2 = x1 + 1
                    y1 = 0
                    y2 = y1 + 1
                    z = 1
                if y1==2 and z==0:
                    x2 += 1
                    y1 = 0
                    y2 = y1 + 1
                    z = 1
                if y2==3 and z==0:
                    y1 += 1
                    y2 = y1 + 1
                    z = 1
                if z==0:
                    y2 += 1
            #sprawdzam czy rząd wynosi 1
            for i in range(0, macierz.shape[0]):
                for j in range(0, macierz.shape[1]):
                    if macierz[i][j]!=0:
                        return 1
            #rząd wynosi 0
            return 0


# In[2]:


A = np.array([[1, 1, 5], [2, 0, 6], [8, 3, 2]])
print(rzad_macierzy(A))
print(np.linalg.matrix_rank(A))


# In[3]:


B = np.array([[3, -1, 1], [5, 1, 4], [-1, 3, 2]])
print(rzad_macierzy(B))
print(np.linalg.matrix_rank(B))


# In[4]:


C = np.array([[1, 3, -2, 4], [1, -1, 3, 5], [0, 1, 4, -2], [10, -2, 5, 1]])
print(rzad_macierzy(C))
print(np.linalg.matrix_rank(C))


# In[5]:


D = np.array([[2, 8, 3, -4], [1, 4, 1, -2], [5, 20, 0, -10], [-3, -12, -2, 6]])
print(rzad_macierzy(D))
print(np.linalg.matrix_rank(D))

