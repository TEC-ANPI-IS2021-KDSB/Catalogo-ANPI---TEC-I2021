%% Requiere la libreria miscellaneous: pkg install -forge miscellaneous


%% Ejemplo numerico
function [approx,err] = cuad_gaussiana (f,n,a,b)
  pkg load miscellaneous
  f = @(x) 4/(1+x^2);
  [aprox, error] = cuad_gaussiana_aux(f,20,0,1)
endfunction

%{
Entradas:
f: Funcion a la que se le quiere calcular la integral
n: Numero de orden
a: Principio del intervalo
b: Final del intervalo
Salidas:
approx: Aproximacion de la integral de f en el intervalo [a,b]
error: Aproximacion del error de la integral 
%}

function [approx,error] = cuad_gaussiana_aux (f,n,a,b)
  polLegendre = legendrepoly(n);
  r = roots(polLegendre);
  r = sort(r);
  approx = 0;
  derivLegendre = polyder(polLegendre);
  for i = 1: n
    xi = r(i);
    wi = 2/((1-xi^2)*(polyval(derivLegendre,xi))^2);
    approx+= f((b-a)*xi/2+(b+a)/2)*wi;
  endfor
  approx*= (b-a)/2;
  error = abs(approx- quad(f,a,b));
endfunction




