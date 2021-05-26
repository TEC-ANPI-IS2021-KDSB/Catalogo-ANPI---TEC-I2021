% Ejemplo numerico
function trapecio
  pkg load symbolic;
  warning('off','all');
  clc;
  f='ln(x)';
  a=2;
  b=5;
  [aprox,error]=trapecioAux(f,a,b);
  
  display(["El valor aproximado por el metodo es ",num2str(aprox)," con un error de ",num2str(error)]);
  
 end
 
% Funcion auxiliar que aproxima el valor para la integral definida de f en el intervalo [a,b]
% Entradas : 
%      f: Funcion a la cual se le quiere calcular la integral.
%      a: Limite inferior del intervalo sobre el que se quiere calcular la integral.
%      b: Limite superior del intervalo sobre el que se quiere calcular la integral.
% Salida : 
%      aprox : Valor aproximado de la funcion en el intervalo indicado.
%      error: Error de la aproximacion
 
 function[aprox,error]=trapecioAux(f,a,b)
  %Definicion de la variable simbolica x y de la funcion de MatLab f
  x=sym('x');
  f=matlabFunction(sym(f));
  
  %Calculo del valor aproximado.
  aprox=((b-a)/2)*(f(a)+f(b));
  
  %Definicion de la funcion f_2 con la que se pretende calcular el maximo de f''(x) en el intervalo [a,b]
  f_2=function_handle(-1*abs(diff(diff(f,x),x)));
  
  %Calculo de la constante alpha para calcular el error de la aproximacion.
  alpha=-1*f_2(fminbnd(f_2,a,b));
  
  %Calculo del error.
  error=((b-a)^3/12)*alpha;
  return;
 
 end