import numpy as np
from math import *

# Esta funcion toma una matriz y determina si es tridiagonal
# Entradas: A: Matriz a determinar tridiagonalidad
# Salidas: Verdadero o falso, dependiendo de la tridiagonalidad
def is_tridiagonal(a):
    dims=a.shape

    for i in range(dims[0]):
        for j in range(dims[1]):
            if(j>i+1 and a[i,j]!=0):
                return False
            elif(j<i-1 and a[i,j]!=0):
                return False
    return True

# Este metodo calcula la matriz solucion al sistema de ecuaciones Ax=B
# Entradas: a: Matriz de coeficientes
#           b: Matriz de termino independientes
# Salidas: Matriz solucion al sistema
def thomas(a,b):
    if(is_tridiagonal(a)):
        n=len(b)
        a_s=[]
        b_s=[]
        c_s=[]
        d_s=b.transpose();
        p_s=[]
        q_s=[]
        xk =np.zeros((1,n))
        for i in range(n):
            if(i==0):
                a_s.append(0)
                b_s.append(a[i,i])
                c_s.append(a[i,i+1])
            elif(i==n-1):
                a_s.append(a[i,i-1])
                b_s.append(a[i,i])
                c_s.append(0)
            else:
                a_s.append(a[i, i - 1])
                b_s.append(a[i, i])
                c_s.append(a[i, i + 1])
        n=len(b)
        qi=0
        pi=0
        for i in range(n):
            if(i==0):
                p_s.append(c_s[i]/b_s[i])
                q_s.append(d_s[0,i]/b_s[i])

            else:
                if(i!=n-1):
                    p_s.append(c_s[i]/(b_s[i]-p_s[i-1]*a_s[i]))
                    q_s.append((d_s[0,i]-q_s[i-1]*a_s[i])/(b_s[i]-p_s[i-1]*a_s[i]))
                else:
                    q_s.append((d_s[0, i] - q_s[i - 1] * a_s[i]) / (b_s[i] - p_s[i - 1] * a_s[i]))
        for j in range(n-1,-1,-1):
            if(j==n-1):
                xk[0,j]=q_s[j]
            else:
                xk[0,j]=q_s[j]-p_s[j]*xk[0,j+1]
        return xk
    else:
        print("La matriz no es tridiagonal")
        return None

a=np.matrix(([-4,1,0,0,0],
             [1,-4,1,0,0],
             [0,1,-4,1,0],
             [0,0,1,-4,1],
             [0,0,0,1,-4]))
b=np.matrix(([1],
             [1],
             [1],
             [1],
             [1]))

xk=thomas(a,b)
if(xk is not None):
    print("Las soluciones del sistema de ecuaciones son: \nxk="+str(xk))

