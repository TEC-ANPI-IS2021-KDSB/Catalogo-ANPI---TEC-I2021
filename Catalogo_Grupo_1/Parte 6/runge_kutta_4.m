clc clear
# Se usa el paquete symbolic
pkg load symbolic
warning('off','all');

% Funcion que calcula la solucion de una ecuacion diferencial ordinaria
% por medio de runge kutta de orden 4
% Entradas : 
%       f : dy/dx en formato de texto
%       a : inicio del intervalo
%       b : fin del intervalo
%       y0 : valor de y en x = a
%       h : paso en el cual dividir el intervalo
% Salidas : 
%      x : valores de x en la solucion de la ecuacion diferencial
%      y : valores de y en la solucion de la ecuacion diferencial
%      polinomio : polinomio de interpolacion correspondiente

function  [x, y, polinomio] = runge_kutta_4_f(fun, a, b, y0, h)
  # Se declaran los simbolico
  sym 'x';
  sym 'y';
  
  # Se convierte f a una funcion de matlab
  f = matlabFunction(sym(fun));
  
  # Se declaran los arrays de x, y
  x = [a:h:b]';
  m = size(x)(1);
  y = zeros(1, m)';
  
  # Se realiza el metodo iterativo
  y(1) = y0;
  for i=1:m-1
    k1 = f(x(i),y(i));
    k2 = f(x(i)+h/2, y(i)+h*k1/2);
    k3 = f(x(i)+h/2, y(i)+h*k2/2);
    k4 = f(x(i)+h, y(i)+h*k3);
    y(i+1) = y(i) + h*(k1+2*k2+2*k3+k4)/6;
  end
  
  # Se calcula el polinomio de interpolacion
  polinomio = simplify (dd_newton_f(x', y'));
  polinomioMatlab = matlabFunction(polinomio);
  
  # Se muestra el polinomio de interpolacion obtenido
  fplot(polinomioMatlab, [a b]);
  title(strcat('Solución de la ecuación diferencial dy/dx = ', fun, ' ; y(', mat2str(a),') = ', mat2str(y0)));
endfunction


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


# Ejemplo numerico 
[x y polinomio] = runge_kutta_4_f('-x*y+4*x/y', 0, 1, 1, 0.1)