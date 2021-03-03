def aprox_div(a,tol):
# Esta funcion aproxima numericamente el valor de 1/a, donde a es diferente de 0
# Parametros de entrada: a=valor para aproximar su inverso multiplicativo, 
#                        tol=tolerancia
# Parametros de salida:  y=aproximacion numerica de 1/a

    import numpy as np
    
    if a==0:
        y='El valor 1/0 no esta definido'
        return y
    else:
        error=tol+1
        x=0.1;
        while error>tol:
            x_new=x*(2-a*x)
            error=np.abs(x-x_new)       
            x=x_new
        return x

# Ejemplo numerico        
y=aprox_div(7,0.00001)
print(y)