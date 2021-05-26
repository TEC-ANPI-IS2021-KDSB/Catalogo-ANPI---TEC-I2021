import numpy as np
from sympy import *
import math
from numpy.core.umath import maximum, minimum
#Entradas:
#f: Funcion a la que se le quiere aproximar la integral
#   Se espera recibir un string de variable x
#a: inicio del intervalo
#b: final del intervalo
#Salidas:
#approx: Una aproximacion a la integral de f en el intervalo [a,b]
#error: aproximado del error de la integral, devuelve -1 en caso de que no se pueda calcular

def  simpson (f,a,b,x):
    #f = parse_expr(ff)
    #print(f.args) 
    intervalo = True
    approx = 0;
    if a>b:
        intervalo = False #El intervalo que nos dieron era degenerado
        #Invertimos el orden de integracion 
        c = a
        b = a
        a = c
    h = (b-a)/2
    approx = f.subs(x,a)+f.subs(x,b)+4*f.subs(x,(a+b)/2)
    approx *= h/3  
    if(intervalo == False): 
        #Cambiamos el signo de la integral en caso de que el intervalo fuera degenerado
        approx*=-1
    error  = h**5/90
    try:
        derivadaCuarta = f.diff(x)
        derivadaCuarta = derivadaCuarta.diff(x)
        derivadaCuarta = derivadaCuarta.diff(x)
        derivadaCuarta = derivadaCuarta.diff(x)
        approxMaximo = abs(derivadaCuarta.subs(x,a))
        for i in range(1,10000):
            approxMaximo = max(approxMaximo,derivadaCuarta.subs(x,a+(b-a)/10000*i))
        error*= approxMaximo
    except:
        error = -1
    return approx,error;

x = Symbol('x')
print(simpson(x**2+1,0,np.pi,x))