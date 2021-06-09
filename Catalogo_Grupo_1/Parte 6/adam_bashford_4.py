import numpy as np
import matplotlib as plt
from sympy import Symbol, sympify, symbols
from sympy.core.sympify import SympifyError


def adam_bashford_4(f, interv, h, yo):
    
    # Almacenando los valores frontera de x
    xi = interv[0]
    xf = interv[1]

    # Calculando el numero de pasos
    npasos = (xf - xi)/h

    # Inicializando los vectores de coordenadas xk y yk
    xk = np.linspace(xi,xf,npasos)
    yk = np.zeros(npasos)

    x = symbols('x','y')
    try:
        f = sympify(f)
    except SympifyError:
        print('Función ingresada invalida')

    # Evaluando los primeros 4 puntos
    yk[0] = yo
    
    yk[1] = f.subs({'x':xk[0], 'y':yk[0]})
    # Adam - Bashford de segundo orden
    yk[2] = yk[1] + h/2*(3*f.subs({'x':xk[1], 'y':yk[1]}) - f.subs({'x':xk[0], 'y':yk[0]}))

    # Adam - Bashford de tercer orden
    yk[3] = yk[2] + h/12*(23*f.subs({'x':xk[2], 'y':yk[2]}) - 16*f.subs({'x':xk[1], 'y':yk[1]}) + 5*f.subs({'x':xk[0], 'y':yk[0]}))

    # Ejecutando el metodo Adam - Bashford de cuarto orden
    for i in range(3, npasos-1):
        yk[i+1] = yk[i-1] + h/24*(55*f.subs({'x':xk[i], 'y':yk[i]}) - 59*f({'x':xk[i-1], 'y':yk[i-1]}) + 37*f({'x':xk[i-2], 'y':yk[i-2]}) - 9*f({'x':xk[i-3], 'y':yk[i-3]}))

    plt.plot(xk,yk)
    plt.xlabel('xk')
    plt.ylabel('yk')
    plt.title('Grafica del polinomio de interpolacion')

    a_s = divided_diff(xk, yk)[0, :]
    poly = print_poly(a_s, x, npasos)
            

    return xk, yk, poly


def divided_diff(x, y):
    '''
    function to calculate the divided
    differences table

    Source: https://pythonnumericalmethods.berkeley.edu/notebooks/chapter17.05-Newtons-Polynomial-Interpolation.html

    '''
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
    p = []

    for i in range(2*n+2):
        p.append('{}'.format(Coef[i]))
    contador = 0
    for k in range(len(x)):
        for i in range(k+contador, 2*n + 1):
            p[i + 1] = p[i + 1] + '*(x-{})'.format(x[k])
        
        for j in range(k+contador+1, 2*n + 1):
            p[j + 1] = p[j + 1] + '*(x-{})'.format(x[k])
        
        contador += 1
    pol = "p(x) = " + "+".join(p)