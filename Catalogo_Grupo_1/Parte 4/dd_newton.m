clc clear
# Se usa el paquete symbolic
pkg load symbolic
warning('off','all');

% Funcion que calcula el polinomio de interpolacion por
% medio de las diferencias divididas de newton
% Entradas : 
%       x_v : vector de valores del eje x para los puntos 
%       y_v : vector de valores del eje y para los puntos 
% Salidas : 
%      polinomio : polinomio de interpolacion correspondiente

function polinomio = dd_newton_f(x_v, y_v)
  n = size(x_v)(2);
  x = sym("x");
  polinomio = 0;
  # Se calcula iterativamente cada monomio del polinomio
  for i=1:n
    s = 1;
    # Se multiplican los valores (x-xn) correspondiente
    for j=1:i-1
      s = s*(x-x_v(j));
    endfor
    # Se suma al polinomio
    polinomio += f(x_v(1:i), x_v, y_v)*s;
  endfor
endfunction

# Funcion auxiliar que calcula el valor de la funcion f, 
# según se define en la presentación de polinomios de interpolación
# Entradas:
#       x : vector de entradas de la funcion matematica
%       x_v : vector de valores del eje x para los puntos a interpolar
%       y_v : vector de valores del eje y para los puntos a interpolar
# Salida:
#       f : valor de la evaluacion
function f = f(x, x_v, y_v)
  n = size(x)(2);
  if(n == 1)
    #Si x tiene un solo valor, se encuentra el valor de y_v al que corresponde
    f = y_v(find(x_v == x(1)));
  else
    # Si x tiene mas de un valor, se aplica la formula matematica
    f = (f(x(2:n), x_v, y_v)-f(x(1:n-1), x_v, y_v))/(x(n)-x(1));
  endif
endfunction

# Ejemplo numérico para los puntos (-2, 0), (0, 1), (1, -1)
simplify (dd_newton_f([-2 0 1], [0 1 -1]))
# Ejemplo numérico para los puntos (1, 2/3), (3, 1), (5, -1), (6, 0)
simplify (dd_newton_f([1 3 5 6], [2/3 1 -1 0]))