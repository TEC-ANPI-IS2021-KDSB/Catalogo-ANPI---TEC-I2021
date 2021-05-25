import numpy as np
import sympy as S
from scipy import optimize

# Se usan las librerias numpy, sympy, scipy y scikit-optimize

# Funcion para calcular una integral mediante la regla compuesta de simpson
# Entradas: 
#       funcion : la funcion a integrar en string
#       n_puntos : número de puntos en los cuales dividir el intervalo
#       intervalo : tupla que indica el intervalo de integración
# Salida:
#       integral: resultado de la integración
#       error: cota de error de la aproximación
def simpson_compuesto(funcion, n_puntos, intervalo):
    # Se establece el simbolo x
    x = S.symbols("x")
    # Se lee la funcion y se deriva
    funcion = S.sympify(funcion)
    f4 = S.diff(funcion, x, 4)
    # Se convierte a funcion de python
    funcion = S.lambdify(x, funcion)
    f4_abs = S.lambdify(x, -abs(f4))

    # Se establecen los valores iniciales
    a = intervalo[0]
    b = intervalo[1]
    x = np.linspace(a, b, num=n_puntos)
    h = x[1]-x[0]
    suma_par = 0
    suma_impar = 0
    n = n_puntos-1
    # Se calcula la integracion
    for i in range(1,int(n/2)):
        suma_par += funcion(x[2*i])
    for i in range(1,int(n/2)+1):
        suma_impar += funcion(x[2*i-1])

    integral = (h/3)*(funcion(x[0]) + 2*suma_par + 4*suma_impar + funcion(x[n]))
    
    # Se calcula el maximo de la cuarta derivada de f en el intervalo
    f4_abs_max = -optimize.minimize_scalar(f4_abs, bounds=(a, b), method='bounded').fun
    # Se calcula el error
    error = ((b-a)*h**4/180)*f4_abs_max
    return (integral, error)

# Ejemplo Numérico
funcion = "ln(x)"
puntos = 7
intervalo = (2,5)
resultado = simpson_compuesto(funcion, puntos, intervalo)
print("Funcion: "+funcion+" | Puntos: "+str(puntos)+" | Intervalo: "+str(intervalo))
print("Resultado: "+str(resultado[0])+" | Error: "+str(resultado[1]))