import numpy as np
import sympy as S
import matplotlib.pyplot as plt

# Funcion para calcular la solucion de un problema de Cauchy
# Entradas:
#       func: la funcion f tal que y'=f(x,y)
#       a: inicio del intervalo
#       b: final del intervalo
#       h: Paso 
#       yo: Valor inicial de y cuando x=a
# Salidas: 
#       Vector xk y yk que representan los pares ordenados del polinomio de interpolacion 
#       Polinomio de interpolacion que es la respuesta al problema de Cauchy 
#       Grafica del polinomio de interpolacion
def predictor_corrector(func,a,b,h,yo):
  # Symbolic
  x = S.symbols("x")
  y = S.symbols("y")
  funcion = S.sympify(func)
  f = S.lambdify([x,y],funcion)

  N = int((b-a)/h) + 1
  yk = np.zeros(N)
  yk[0] = yo
  xk = np.zeros(N)
  xk[0] = a
  
  val = a
  index = 0
  while index < N:
    xk[index] = val
    index+=1
    val+= h
  
  k=0
  while k <= N-2:
    ybar = yk[k] + h*f(xk[k],yk[k])
    yk[k+1] = yk[k] + h*(f(xk[k],yk[k])+f(xk[k+1],ybar))/2
    k += 1
  
  # Grafica del polinomio de interpolacion
  plt.plot(xk,yk)
  plt.show()

  a_s = divided_diff(xk,yk)[0,:]
  x = S.symbols('x,y')
  poly = S.simplify(S.sympify(print_poly(a_s,xk,N)))

  # Falta el polinomio de interpolacion
  return [xk,yk,poly]

# Metodo que calcula los coeficientes del polinomio de interpolacion
# a partir del método de diferencias divididas de newton
# Entradas: x: Vector de valores de x por los que debe pasar el polinomio
#           y: Vector de valores de y por los que debe pasar el polinomio 
# Salidas:  Vector de coeficientes a_s del polinomio de interpolacion
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

# Metodo que se encarga de imprimir el polinomio de interpolacion
# a partir de la lista de coeficientes del mismo
# Entradas: Coef: Coeficientes a_s del polinomio de interpolacion
#           x: Vector de valores de x
#           n: Longitud de x 
# Salidas: polinomio de interpolación 
def print_poly(Coef, x, n):
    p = []

    for i in range(n):
        p.append('{}'.format(Coef[i]))
    contador = 1
    for k in range(len(x)):
        for i in range(k+contador, n):
            p[i] = p[i] + '*(x-{})'.format(x[k])
        
        # for j in range(k+contador+1, n-1):
        #     p[j + 1] = p[j + 1] + '*(x-{})'.format(x[k])
        
        # contador += 1
    pol = "+".join(p)
    return pol

# Ejemplo Numerico 

ejemplo = predictor_corrector('y-x^2+1',0,2,(2/(11-1)),0.5)
x = ejemplo[0]
y = ejemplo[1]
pol = ejemplo[2]
print("\nVector x: "+ str(x))
print("\nVector y: "+ str(y))
print("\nPolinomio: "+ str(pol))