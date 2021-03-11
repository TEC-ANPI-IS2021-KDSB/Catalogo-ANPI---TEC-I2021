import sympy as S
import matplotlib.pyplot as plt


# Funcion para calcular ceros de funcion con el Metodo del Punto Fijo
# Entradas: 
#       funcion : la funcion 
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
    error= float('inf')

    #Se inicializan el plot
    fig, ax = plt.subplots()

    fig.suptitle("Error en el Método de Punto Fijo")
    plt.xlabel("Iteraciones")
    plt.ylabel("Error")

    try:
        #Se agrega el primer error
        error=funcion(x_k)
        ax.scatter(1, error, s=6, c="red")
        plt.pause(0.01)

        # Se itera
        for k in range(0, iterMax):

            # Se calcula el valor de la siguiente aproximación
            x_k = funcion(x_k)
            error = funcion(x_k)

            #Se actualiza el plot
            ax.scatter(k+2, error, s=6, c="red")
            plt.pause(0.01)

        plt.show()
    except:
        pass

    # Se retorna el cero y el error
    return [x_k, error]


def prueba():
    [x_k, error] = punto_fijo("sin(x)", 2, 50)
    print("Error: " + str(error) + " |  Cero: " + str(x_k))

def __main__():
    prueba()

__main__()