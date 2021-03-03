function ejemplo_lenguaje_m
  % Ejemplo numerico        
  clc; clear;
  a=7; tol=10^-5;
  y=aprox_div(a,tol)
end

function y=aprox_div(a,tol)
  % Esta funcion aproxima numericamente el valor de 1/a, donde a es diferente de 0
  % Parametros de entrada: a=valor para aproximar su inverso multiplicativo, tol=tolerancia
  % Parametros de salida: y=aproximacion numerica de 1/a
  if a==0
    y='El valor 1/0 no está definido';
  else    
    error=tol+1;
    x=0.1;
    while error>tol
      x_new=x*(2-a*x);
      error=abs(x-x_new);
      x=x_new;
    end
    y=x;
  end
end
