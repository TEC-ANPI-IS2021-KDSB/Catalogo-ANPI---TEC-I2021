import numpy as np
import sympy as S
from scipy import optimize
# Se usan las librerias numpy, sympy, scipy y scikit-optimize

# Funcion para calcular la cota de error del trazador cubico
# Entradas: 
#       funcion : la funcion que se aproxima (en texto)
#       puntos : array de python del conjunto soporte
# Salida:
#       cota de error de un trazador cubico
def cota_traz_cubico(funcion, puntos):
    # Se crean los simbolicos
    x = S.symbols("x")
    funcion = S.sympify(funcion)
    # Se calcula la cuarta derivada
    f4 = S.diff(funcion, x, 4)
    # Se crea una funcion de python del valor absoluto de f4 y se multiplica por -1
    f4_abs = S.lambdify(x, -abs(f4))
    # Se calcula el minimo de f4_abs, lo cual equivale al maximo de f4, en el intervalo de los puntos
    f4_norm_inf = optimize.minimize_scalar(f4_abs, bounds=(puntos[0],puntos[len(puntos)-1]), method='bounded').x
    
    # Se convierten los puntos en un array de numpy
    puntos = np.array(puntos)
    # Se calcula la constante h
    h = (puntos[1:len(puntos)] - puntos[0:len(puntos)-1]).max()

    # Se retorna la operacion final
    return 5*(h**4)*f4_norm_inf/384

# Ejemplo numerico
print('Lo cota para ln(x+1), S =  [1, 2, 2.5, 3], es: \n' + str(cota_traz_cubico('ln(x+1)', [1, 2, 2.5, 3])))