import numpy as np
from math import *
import random
import matplotlib.pyplot

'''
    Funcion desarrollada para realizar la sustitucion hacia atras en una matriz triangular inferior.
    
    Entradas: a=Matriz de coeficientes. 
              b=Vector de terminos independientes.
              
    Salidas: xk=Vector columna de soluciones que se obtiene de resolver el sistema formado por ax=b.
'''
def sust_atras(a,b):
    n = len(b)
    xk = np.zeros((1, n))
    for i in range(n):
        suma = 0
        for j in range(i):
            suma += a[i, j] * xk[0, j]
        xi = (1 / a[i, i]) * (b[i] - suma)
        xk[0, i] = xi
    return np.asmatrix(xk).transpose()

'''
    Funcion desarrollada para determinar si una matriz es simetrica.
    
    Entradas: a= Matriz a analizar.
    
    Salidas:  Booleano resultante de analizar la matriz a.
'''
def is_symetric(a):
    dims=a.shape
    a_t=a.transpose()
    for i in range(dims[0]):
        for j in range(dims[1]):
            if(a[i,j]!=a_t[i,j]):
                print("La matriz no es simetrica!")
                return False
    return True


'''
    Funcion desarrollada para determinar si una matriz es positiva definida.

    Entradas: a= Matriz a analizar.

    Salidas:  Booleano resultante de analizar la matriz a.
'''
def is_positive_defined(a,n):
    dims = a.shape
    n = dims[0]
    for i in range(n):
        temp = a[0:i + 1, 0:i + 1]
        if (np.linalg.det(temp) < 0):
            print("La matriz no es positiva definida!")
            return False
    return True


'''
    Funcion que implementa el metodo de relajacion estudiado.
    
    Entradas: 
              a= Matriz de coeficientes.
              b=Matriz de terminos independientes.
              x0=Vector columna de valores x iniciales.
              tol=Tolerancia permitida para el metodo.
              iterMax= Numero de iteraciones maximas a realizar.
    Salidas:
              xk=Vector de valores en x que representan la solucion del sistema de ecuaciones descrito por ax=b.
              error=Error obtenido del resultado xk encontrado.
              k= Numero de iteraciones que le tomo al metodo para encontrar la solucion xk.
'''
def relajacion(a,b,x0,tol,iterMax):
    dims = a.shape
    n = dims[0]

    #Verificacion para determinar si a es cuadrada.
    if(dims[0]!=dims[1]):
        print("La matriz no es cuadrada!")
        return (None,None,None)
    #Verificacion para determinar si a es simetrica,invertible y positiva definida.
    if(np.linalg.det(a)!=0 and is_symetric(a) and is_positive_defined(a,n)):

        # Definicion de un valor random para w en ]0,2[.
        w=0
        while(w==2 or w==0):
            w=random.uniform(0,2)

        #Definicion de los valores D,L,U.
        d=np.asmatrix(np.diag(np.diag(a)))
        l=np.asmatrix(np.tril(a,-1))
        u=np.asmatrix(np.triu(a,1))

        #Valor que acompana la incognita en el sistema de ecuaciones e*zK=f.
        e=d+w*l

        #Valor del sistema de ecuaciones e*zK=f.
        f=((1-w)*d-w*u)*x0

        #Resolucion del sistema de ecuaciones e*zK=f.
        zk=sust_atras(e,f)

        #Valor del sistema de ecuaciones e*c=g.
        g=w*b

        #Resolucion del sistema de ecuaciones e*c=g.
        c=sust_atras(e,g)

        k=1
        xk=x0
        iteraciones=[]
        errores=[]

        #Ciclo iterativo para realizar las iteraciones requeridas por el metodo para aproximar xk.
        while(k<iterMax):
            #Recalculado los valores f y zk.
            f=((1-w)*d-w*u)*xk
            zk = sust_atras(e,f)

            #Calculando x_k+1.
            xk=zk+c

            #Calculo del error asociado a la iteracion actual.
            error=np.linalg.norm(a*xk-b)

            #Verificacion de la condicion de parada asociada a la tolerancia definida.
            if(error<=tol):
                break
            k+=1
            iteraciones.append(k)
            errores.append(error)
            
       #Graficacion de los errores
        matplotlib.pyplot.plot(iteraciones,errores)
        matplotlib.pyplot.ylabel("Errores |f(Xk)|")
        matplotlib.pyplot.title("Graficación Errores vs Iteraciones")
        matplotlib.pyplot.xlabel("Iteración")
        
        return (xk,error,k)

    return (None,None,None)


#---> Caso de ejemplo <---#

a=np.matrix(([4,3,0],
             [3,4,-1],
             [0,-1,4]))
b=np.matrix(([24],
             [30],
             [-24]))

x0=np.asmatrix(np.zeros(a.shape[0])).transpose()
tol=1e-10
iterMax=2500
valores=relajacion(a,b,x0,tol,iterMax)
if(valores[0] is not None):
    print("Las soluciones del sistema de ecuaciones obtenidas en "+str(valores[2])+" iteraciones con un error de "+str(valores[1])+" son: \nxk="+str(valores[0].transpose()))
    matplotlib.pyplot.show()
    

