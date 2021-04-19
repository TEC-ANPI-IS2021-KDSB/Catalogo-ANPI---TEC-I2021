import numpy as np

#Librerías: Se usa la libreria numpy

# Funcion para calcular la solucion de un sistema de ecuaciones de acuerdo
# al método de la factorización LU
# Entradas: 
#       A : matriz de numpy del sistema a resolver
#       b : vector de numpy para el cual resolver el sistema
# Salida:
#       x : vector de solucion

def fact_lu(A,b):
    [m, n] = A.shape
    [k,] = b.shape

    if not verificacion_lu(A):
        return np.zeros(b.shape)
    elif k!=m:
        return np.zeros(b.shape)
    else:
        (L,U) = fact_lu_aux(A)
        y = sustitucion_adelante(L, b)
        x = sustitucion_atras(U, y)
        return x

# Funcion para verificar si la matriz de entrada cumple las condiciones para la
# factorizacion LU.
# Entradas: 
#       A : matriz de numpy del sistema a resolver
# Salida:
#       booleano : indica si A cumple las condiciones

def verificacion_lu(A):
    [a,b] = A.shape
    if a!=b :
        return False
    for i in range(1,a):
        if(det(A[0:i,0:i])==0):
            return False
    return True

# Funcion para realizar la factorización LU de una matriz
# Entradas: 
#       A : matriz de numpy a la cual calcular la factorizacion LU
# Salida:
#       L : matriz L de la factorizacion
#       U : matriz U de la factorizacion
def fact_lu_aux(A):
    [a, b] = A.shape
    U = A.astype(np.float64)
    L = np.zeros(A.shape)
    np.fill_diagonal(L, 1)
    for j in range(b):
        for i in range(j+1,a):
            x = U[i, j]/U[j, j]
            U[i,0:b] -= x*U[j, 0:b]
            L[i, j] = x
    return (L,U)

# Funcion para realizar la sustitucion hacia adelante en un sistema de ecuaciones
# triangular inferior
# Entradas: 
#       A : matriz de numpy triangular inferior
#           a la aplicarle la sustitucion hacia adelante
#       b : vector de numpy para el cual resolver el sistema
# Salida:
#       x : solucion del sistema
def sustitucion_adelante(A, b):
    [n, m] = A.shape
    x = np.zeros(m)
    for i in range(n):
        x[i] = (b[i] - np.dot(A[i,0:m],x))/A[i,i]
    return x

# Funcion para realizar la sustitucion hacia atras en un sistema de ecuaciones
# triangular superior
# Entradas: 
#       A : matriz de numpy triangular superior
#           a la aplicarle la sustitucion hacia atras
#       b : vector de numpy para el cual resolver el sistema
# Salida:
#       x : solucion del sistema
def sustitucion_atras(A, b):
    [n, m] = A.shape
    x = np.zeros(m)
    for i in range(-(n-1),1):
        x[-i] = (b[-i] - np.dot(A[-i,0:m],x))/A[-i,-i]
    return x

# Funcion para calcular el determinante de una matriz cuadrada
# Entradas: 
#       A : matriz de numpy cuadrada
# Salida:
#       determinante : determinante de A
def det(A):
    [a,b] = A.shape
    determinante = 0
    sign = 1
    if b == 1:
        determinante = A[0,0] 
    else:
        for i in range(b):
            determinante += sign*A[0, i]*det(np.concatenate((A[1:a,0:i], A[1:a,i+1:b]), axis=1))
            sign = -1*sign
    return determinante

#Ejemplo Numérico
A = np.array([[4,-2, 1],
              [20,-7, 12], 
              [-8, 13, 17]])
b = np.array([11,70,17])
x = fact_lu(A, b)
print("Matriz: ")
print(A)
print("\nVector b: ")
print(b)
print("\nSolucion x: ")
print(x)
