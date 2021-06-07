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
  print(N)
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

  # Falta el polinomio de interpolacion
  return [xk,yk]

print(predictor_corrector('y-x^2+1',0,2,(2/(11-1)),0.5))