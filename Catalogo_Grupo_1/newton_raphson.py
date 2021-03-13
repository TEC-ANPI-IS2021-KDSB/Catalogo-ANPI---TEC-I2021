#Importamos las siguientes librerias para que se reconozca cualquier expresion que se introduzca. 
from sympy import *
from sympy.parsing.sympy_parser import parse_expr #libreria para parsear
import matplotlib.pyplot #libreria para graficar, utilizamos pyplot de matplotlib
from math import * #Libreria matematica
 
#funcion:La funcion debe ir en formato de string para evitar errores.
#ValorInicial:es el valor inicial de la aproximacion
#tolerancia:tolerancia que se definira para la aproximacion

############################################################################################################################################
#Funcion principal
def newton_raphson(funcion,ValorInicial,tolerancia):
    newton_raphson_secundaria(funcion,ValorInicial,tolerancia,[]) #Se crea un vector para guardar los valores
############################################################################################################################################
#Funcion secundaria para el calculo
def newton_raphson_secundaria(funcion,ValorInicial,tolerancia,Conjunto_Valores):
    Conjunto_Valores.append(abs(ValorInicial)) #Se añade  el valor absoluto del valor inicial al vector
    #El ultimo valor sera la resta del valor inicial menos el cosiente de la evaluacion de la funcion con el valor inicial entre la evaluacion de la derivada de la funcion con el valor inicial
    Ultimo_Valor =ValorInicial-(EvaluacionGlobal(funcion,ValorInicial)/Evaluacion_De_Derivada(funcion,ValorInicial)) 

    
    if abs(EvaluacionGlobal(funcion,Ultimo_Valor))<=tolerancia: #Verifica si la evaluacion de la funcion con el ultimo valor es menor o igual a la tolerancia
        #Añade el ultimo valor al vector de valores
        Conjunto_Valores.append(Ultimo_Valor) 
        print(Ultimo_Valor) #Muestra el ultimo valor
        #Graficacion de los errores
        matplotlib.pyplot.plot(Conjunto_Valores)
        #Label de grafica para texto de "errores"
        matplotlib.pyplot.ylabel("Errores |f(Xk)|")
        #Label de grafica para texto de "Graficacion"
        matplotlib.pyplot.title("Graficación Errores vs Iteraciones")
        #Label de grafica para texto de "Iteracion"
        matplotlib.pyplot.xlabel("Iteración")
        #Se muestra la grafica 
        matplotlib.pyplot.show()
        
        #Si no cumple la verificacion retorna a la funcion con el ultimo valor en lugar del valor inicial
    else:
        newton_raphson(funcion,Ultimo_Valor,tolerancia) 

############################################################################################################################################
#Modulo de evaluacion        
def EvaluacionGlobal(funcion,x):#Recibe la funcion y un valor
    return eval(funcion) #se analiza la expresion de la funcion

############################################################################################################################################
#Modulo de evaluacion de derivada
#En este modulo se evalua la derivada parseando la funcion
def Evaluacion_De_Derivada(funcion,x): #Recibe la funcion y un valor
    expresion = parse_expr(funcion) #Se parsea la funcion y se guarda en "expresion"
    derivada = expresion.diff(Symbol('x')) 
    return eval(str(derivada))



#Para ejecturar en la ventana de comandos basta con utilizar: newton_raphson("funcion",ValorInicial,tolerancia) y cambiar valores a estudiar
