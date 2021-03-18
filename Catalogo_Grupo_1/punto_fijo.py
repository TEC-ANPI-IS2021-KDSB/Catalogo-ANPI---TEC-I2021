import sympy as S
import matplotlib.pyplot as plt

# Utiliza las librerías sympy y matplotlib


# Funcion para calcular ceros de funcion con el Metodo del Punto Fijo
# Entradas: 
#       funcion : la funcion en texto
#       valorInicial : estimacion del cero
#       iterMax : iteraciones maximas
# Salidas:
#       [cero aproximado, error]

def punto_fijo(funcion, valorInicial, iterMax):
    # Se establece el simbolo x
    x = S.symbols("x")
    # Se lee la funcion
    funcion = S.sympify(funcion)
    # Se convierte a funcion de python
    funcion = S.lambdify(x, funcion)

    # Se inicializan los valores de la iteración y el array de errores
    x_k = valorInicial
    error_array= [float('inf')]

    try:
        #Se agrega el primer error
        error_array=[funcion(x_k)]

        # Se itera
        for k in range(0, iterMax):

            # Se calcula el valor de la siguiente aproximación
            x_k = funcion(x_k)
            error_array.append(funcion(x_k))
    except:
        pass

    #Se inicializan el plot
    fig, ax = plt.subplots()

    fig.suptitle("Error en el Método de Punto Fijo")
    plt.xlabel("Iteraciones")
    plt.ylabel("Error")

    #Se actualiza el plot
    ax.scatter(list(range(1,k+3)), error_array, s=6, c="red")        
    plt.show()

    # Se retorna el cero y el error
    return [x_k, error_array[-1]]


# Ejemplo Numerico
def prueba():
    [x_k, error] = punto_fijo("sin(x)", 2, 1000)
    print("Error: " + str(error) + " |  Cero: " + str(x_k))

prueba()
