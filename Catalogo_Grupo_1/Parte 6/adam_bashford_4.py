import numpy as np
import matplotlib.pyplot as plt
from sympy import Symbol, sympify, symbols
from sympy.core.sympify import SympifyError

def divided_diff(x, y):
    
    # Funcion que calcula la tabla de
	# diferencias finitas
	
	# x: Vector de coordenadas x
	# y: Vector de coordenadas y

    # Source: https://pythonnumericalmethods.berkeley.edu/notebooks/chapter17.05-Newtons-Polynomial-Interpolation.html

    n = len(y)
    coef = np.zeros([n, n])
    # the first column is y
    coef[:,0] = y
    
    for j in range(1,n):
        for i in range(n-j):
            coef[i][j] = \
            (coef[i+1][j-1] - coef[i][j-1]) / (x[i+j]-x[i])
            
    return coef

def print_poly(Coef, x, n):

    # Funcion que imprime en formato string el polinomio de interpolacion
    # calculado por el metodo de Newton

    # Coef: Vector de coeficientes del polinomio
    # x: Vector de coordenadas x del dominio del polinomio
    # n: numero de puntos utilizados para construir el polinomio de interpolacion

    p = []

    for i in range(n):
        p.append('{}'.format(Coef[i]))
    contador = 0
    for k in range(n):
        for i in range(k, n-1):
            p[i + 1] = p[i + 1] + '*(x-{})'.format(x[k])
       
    pol = "p(x) = " + "+".join(p)
    return pol

def adam_bashford_4(f, interv, h, yo):

	# f: Funcion del tipo f(x,y) en formato string, siguiendo la nomenclatura matematica de Python
	# interv: Lista con los valores frontera en x con la forma: [xi, xf]
	# h: tamaño de paso 
	# yo: Valor inicial de la solucion para y(x=0) 
	
	# La funcion adam_bashford_4 utiliza la formula de cuarto orden de Adam - Bashford
	# para hacer la mayoria de los calculos dentro del intervalo necesario.
	# Los primeros 4 valores de la solucion, a excepcion del inicial yo, son calculados con
	# las formlas de Adam - Bashford de orden inferior hasta alcanzar la formula de cuarto orden
	
	# La funcion requiere de las librerias: Numpy, Matplotlib, y Sympy para funcionar
	# La salida de la funcion es:
	# xk: coordenadas x evaluadas
	# yk: coodernadas y obtenidas
	# poly: polinomio de interpolacion en formato string
    
    # Almacenando los valores frontera de x
    xi = interv[0]
    xf = interv[1]

    # Calculando el numero de pasos
    npasos = int((xf - xi)/h)

    # Inicializando los vectores de coordenadas xk y yk
    xk = np.linspace(xi,xf,npasos)
    yk = np.zeros(npasos)

    x = symbols(('x','y'))
    try:
        f = sympify(f)
    except SympifyError:
        print('Función ingresada invalida')

    # Evaluando los primeros 4 puntos
    yk[0] = yo
    
    # Metodo de Euler
    yk[1] = yk[0] + h*f.subs({'x':xk[0], 'y':yk[0]})
    # Adam - Bashford de segundo orden
    yk[2] = yk[1] + h/2*(3*f.subs({'x':xk[1], 'y':yk[1]}) - f.subs({'x':xk[0], 'y':yk[0]}))

    # Adam - Bashford de tercer orden
    yk[3] = yk[2] + h/12*(23*f.subs({'x':xk[2], 'y':yk[2]}) - 16*f.subs({'x':xk[1], 'y':yk[1]}) + 5*f.subs({'x':xk[0], 'y':yk[0]}))

    # Ejecutando el metodo Adam - Bashford de cuarto orden
    for i in range(3, npasos-1):
        yk[i+1] = yk[i] + h/24*(55*f.subs({'x':xk[i], 'y':yk[i]}) - 59*f.subs({'x':xk[i-1], 'y':yk[i-1]}) + 37*f.subs({'x':xk[i-2], 'y':yk[i-2]}) - 9*f.subs({'x':xk[i-3], 'y':yk[i-3]}))

    plt.plot(xk,yk)
    plt.xlabel('xk')
    plt.ylabel('yk')
    plt.title('Grafica del polinomio de interpolacion')
    plt.show()

    # # Invocando la funcion que calcula las diferencias finitas por el metodo de Newton
    a_s = divided_diff(xk, yk)[0, :]
	# # Invocando la funcion que imprime el polinomio de interpolacion
    poly = print_poly(a_s, xk, npasos)
    return xk, yk, poly

# Ejemplo numerico

fxy = '1+(x-y)**2'
h = 0.2
y0 = 1
Intervalo = [2,4]

xn,yn,pol = adam_bashford_4(fxy, Intervalo, h, y0)
print(pol)
