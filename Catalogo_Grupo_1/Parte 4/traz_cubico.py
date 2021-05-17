import numpy as np
from math import *
from sympy import *

#Metodo de Thomas para resolucion de sistemas de ecuaciones
def is_tridiagonal(a):
    dims=a.shape

    for i in range(dims[0]):
        for j in range(dims[1]):
            if(j>i+1 and a[i,j]!=0):
                return False
            elif(j<i-1 and a[i,j]!=0):
                return False
    return True
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

# Funcion para calcular los trazadores cubicos para un juego de puntos dados
# Entradas: 
#       points: Lista de tuplas que representan los puntos para el calculo
# Salida:
#       Lista con los trazadores encontrados

def traz_cubico(points):
    #Generacion del vector de intervalos h
    h=[]
    for ind in range(len(points)-1):
        h.append(points[ind+1][0]-points[ind][0])

    #Generacion de la matriz tridiagonal A
    a=[]
    for ind in range(len(h)-1):
        row=[]
        for ind2 in range(ind-1):
            row.append(0)
        if(ind!=0):
            row.append(h[ind])
        row.append(2*(h[ind]+h[ind+1]))
        if(ind!=len(points)-3):
            row.append(h[ind+1])
        for ind2 in range(len(points)-4):
            row.append(0)
        a.append(row)

    #Generacion del vector u
    u=[]
    for ind in range(len(h)-1):
        u.append(6*(((points[ind+2][1]-points[ind+1][1])/(h[ind+1]))-((points[ind+1][1]-points[ind][1])/(h[ind]))))

    a=np.matrix((a))
    u=np.matrix((u)).transpose()
    print(len(u))
    #Resolviendo A*M=u y agregando M0 y Mn
    m=np.append(np.zeros((1,1)),np.append(thomas(a,u),[0]))

    #Se calculan los coeficientes a,b,c,d
    coef=[]
    for ind in range(len(h)):
        a=(m[ind+1]-m[ind])/(6*h[ind])
        b=m[ind]/2
        c=((points[ind+1][1]-points[ind][1])/h[ind])-((h[ind]*(m[ind+1]*2*m[ind]))/6)
        d=points[ind][1]
        coef.append((a,b,c,d))
    #Se calculan los valores simbolicos de S
    x=symbols('x')
    s=[]
    for ind in range(len(h)):
        coefT=coef[ind]
        point=points[ind]
        with evaluate(False):
            s.append(coefT[0]*(x-point[0])**3+coefT[1]*(x-point[0])**2+coefT[2]*(x-point[0])+coefT[3])
    return s

s=traz_cubico([(1,2.718282),(1.05,3.286299),(1.07,3.527609),(1.1,3.905416)])
for valor in s:
    print(valor)
