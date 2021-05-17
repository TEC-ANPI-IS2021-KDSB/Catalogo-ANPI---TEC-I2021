% Caso de prueba
function cota_poly_inter
  cota = cota_poly_inter_aux("sin(pi*x/2)",[-1 0 1 2])
end

% Funcion que calcula la cota de error del polinomio de interpolacion a partir de la funcion
% a la cual se le calcula el polinomio y un conjunto de soporte.
% Entradas: funcion: Funcion a la cual se le va a calcular la cota de error (con x como variable)
%           soporte: Conjunto de soporte sobre el cual se va a calcular la cota de error
% Salidas: Cota de error máxima del polinomio de interpolación.
function [cota] = cota_poly_inter_aux(funcion, soporte)
  % Simbolico
  pkg load symbolic;
  syms x;
  
  fsym = sym(funcion);
  f = matlabFunction(sym(funcion));

  % Variables necesarias
  n = length(soporte);
  a = soporte(1);
  b = soporte(n);
  derivada1 = matlabFunction(diff(fsym));
  derivadan = matlabFunction(diff(fsym, n));
  
  % Aqui hay que calcular el valor de x que maximiza la multiplicacion 
  % |(x-x1)(x-x2)(x-x3)|...

  % Calculando ax y la multiplicacion
  mult = calcXLim(a,b,generarMult(soporte));
  ax = calcXLim(a,b,diff(fsym,n));

  % Calculo final
  cota = (1/(factorial(n)))*ax*mult;

end

% Funcion que calcula el valor limite de una funcion simbolica (es decir el maximo del valor absoluto)
% Entradas: a, minimo del intervalo
%           b, máximo del intervalo
%           f, funcion simbolica
% Salidas: fmax: Valor limite
%          x_max: Un valor de x en el cual se alcanza este valor limite
function [fmax, x_max] = calcXLim(a,b,f)
  pkg load symbolic;
  syms x;
  f1=matlabFunction(f);
  fd = diff(f,x)==0;
  puntos_criticos = double(solve(fd,x))';
  puntos_a_evaluar=[a b puntos_criticos];
  valores_evaluados= [abs(f1(puntos_a_evaluar))];
  [fmax,i_max]=max(valores_evaluados);
  x_max = puntos_a_evaluar(i_max);
end

% Funcion que genera una funcion simbolica del tipo (x-x1)(x-x2)...(x-xn) a partir de un conjunto de soporte
% Entradas: Conjunto soporte
% Salidas: Funcion simbolica del tipo (x-x1)(x-x2)...(x-xn)
function symFMul = generarMult(soporte)
  syms x;
  n = length(soporte);
  symStr = "1";
  for i=1:n
    charS = num2str(soporte(i));
    symStr = strcat(symStr, "*(x-",charS,")");
  end
  symFMul = sym(symStr);
end