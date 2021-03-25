import numpy as np
from sympy import Symbol, Derivative, sympify, pprint
from sympy.core.sympify import SympifyError
from pylab import plot, show, xlabel, ylabel, title, figure

#Definicion de la funcion
def function(f, X):
    x = Symbol('x')
    y = Symbol('y')

    xe = X[0]
    ye = X[1]           
    return f.subs({x:xe, y:ye})

#Gradiente de la funcion
def gradiente(f, X):
    x = Symbol('x')
    y = Symbol('y')
    xs = X[0]
    ys = X[1]  
    fx = Derivative(f, x).doit().subs({x:xs, y:ys})
    fy = Derivative(f, y).doit().subs({x:xs, y:ys})
 
    value = np.array([[fx, fy]])
    return value

# Funcion principal
# Aproxima un minimo mediante el metodo de gradiente conjugado no lineal 
def gcnl(f, Xo, tol, max_it):

    #f es la funcion definida (Definida como una funcion con nombre f)
    #df es el gradiente de la función definida (Definida como una funcion con nombre df)
    #Xo es es array con las coordenadas del primer valor para el metodo iterativo
    #tol es la tolerancia permitida en el error de aproximacion
    #max_it es el maximo numero de iteraciones permitidas 

    
    x = Symbol('x')
    y = Symbol('y')

    try:
        f = sympify(f)
    except SympifyError:
        print('Entrada inválida')
    

    Xn = np.zeros((n, 2))           #
    g = np.zeros((n, 2))            #Array de coordenadas que se calcularán
    d = np.zeros((n, 2))            #Array de las direcciones que se calcularán
    error = np.zeros(n)             #Array de error calculado
    betak = 0                       #Parámetros de actualización Beta_k

    Xn[0][0] = Xo[0][0]
    Xn[0][1] = Xo[1][0]

    g[0] = gradiente(f, Xn[0])             #Cálculo de g_0
    d[0] = -g[0]                    #Cálculo de d_0

    delta = 0.5                     #Valor delta asumido
    contador = 0                    #Variable que contiene el número de iteraciones realizadas

    for i in range(n - 1):
        alpha = 1                   #Valor inicial de alpha

        #Este bucle busca un valor de alpha que satisface la condición f(x_k + alpha*d_k) + alpha*d_k <= delta*alpha*g_k^T*d_k
        while (function(f, Xn[i] + alpha*d[i]) - function(f, Xn[i]) > delta*alpha*np.matmul(g[i].transpose(), d[i])):
            alpha *= 1/2

        Xn[i + 1] = Xn[i] + d[i]*alpha                  #Se calcula un nuevo conjunto de coordenadas
        error[i] = np.linalg.norm(Xn[i + 1] - Xn[i])    #Se calcula el error entre Xk y Xk+1
        contador += 1

        if error[i] <= tol:             #Este bloque lógico comprueba si el error está por debajo de la tolerancia
            break                       #Si es verdadero, entonces el programa sale del bucle for
        else:                           #Si la condición anterior no es true, se ejecutará el siguiente bloque
            g[i+1] = gradiente(f, Xn[i + 1])  
            betak = (np.linalg.norm(g[i + 1]))**2/((np.linalg.norm(g[i]))**2)   #betak calculado con el modelo Fletche y Reeves
            d[i+1] = -g[i + 1] + betak*d[i]
    

    fig = figure()
    plot(list(range(1, contador + 1)), error[:contador], marker = ".")
    xlabel('#Iteraciones')
    ylabel('Error')
    title('Error de aproximacion en cada iteracion')

    print('Aproximacion (x, y) = ({}, {})'.format(Xn[contador][0], Xn[contador][1]))
    print('Error calculado Err = ', error[contador - 1])

    return Xn[contador], fig, error[contador - 1]



f = input('Introduzca la funcion: ')
n = int(input('Introduzca la cantidad máxima de iteraciones: '))                #Numero maximo de iteraciones
xo = float(input('Introduzca la coordenada x del valor inicial: '))
yo = float(input('Introduzca la coordenada y del valor inicial: '))
tolerancia = float(input('Introduzca la tolerancia permitida: '))          #Tolerancia permitida
Xo = np.array([[xo], [yo]])                                           #Coordenadas iniciales


Xn, figura, error = gcnl(f, Xo, tolerancia, n)                        #Llama a la función
show()

