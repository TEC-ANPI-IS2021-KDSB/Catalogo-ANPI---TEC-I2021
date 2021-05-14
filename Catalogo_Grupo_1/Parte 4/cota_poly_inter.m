% Funcion que calcula la cota de error del polinomio de interpolacion a partir de la funcion
% a la cual se le calcula el polinomio y un conjunto de soporte.
% Entradas: funcion: Funcion a la cual se le va a calcular la cota de error (con x como variable)
%           soporte: Conjunto de soporte sobre el cual se va a calcular la cota de error
% Salidas: Cota de error máxima del polinomio de interpolación.
function cota_poly_inter
  cota = cota_poly_inter_aux("sin(pi*x/2)",[-1 0 1 2])
end

function[cota]=cota_poly_inter_aux(funcion, soporte)
  % Simbolico
  pkg load symbolic;
  syms x;
  fsym = sym(funcion);
  f = matlabFunction(sym(funcion));

  % Variables necesarias
  n = length(soporte);
  derivada1 = matlabFunction(diff(fsym));
  derivadan = matlabFunction(diff(fsym, n));
  
  % Calculando la x maxima
  posibleYMax = [f(soporte(1)) f(soporte(n))];
  solDiff = transpose(solve(diff(fsym)==0,x))
  for i=1:length(solDiff)
    posibleYMax = [posibleYMax f(solDiff(i))]
  end
  posibleXMax = solve(fsym==max(posibleYMax),x)
  xMax = solve(fsym==max(posibleYMax),x)(1)

  % Calculando ax y la multiplicacion
  posibleDMax = [];
  mult = 1;
  for i=1:n
    posibleDMax = [posibleDMax derivadan(soporte(i))];
    mult = mult * (xMax-soporte(i))
  end
  ax = max(posibleDMax)

  % Calculo final
  cota = (1/(factorial(n+1)))*ax*mult;

end

function xMax = calcXMax(soporte)
  n = length(soporte);
  symStr = "1"
  for i=1:n
    symStr = strcat(symStr, "*(x-",char(soporte(i)),")")
  end

end


