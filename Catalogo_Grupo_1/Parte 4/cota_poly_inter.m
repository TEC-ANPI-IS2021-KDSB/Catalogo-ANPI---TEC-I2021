function cota = cota_poly_inter(funcion, soporte)
  % Simbolico
  pkg load symbolic;
  syms x;
  fsym = sym(f);
  f = matlabFunction(sym(f));

  % Variables necesarias
  n = length(soporte);
  derivada1 = matlabFunction(diff(funcion));
  derivadan = matlabFunction(diff(funcion, n));
  
  % Calculando la x maxima
  posibleYMax = [f(derivada1(soporte(1))) f(derivada1(soporte(2)))];
  solDiff = transpose(Solve(diff(fsym)==0,x));
  for i=1:length(solDiff)
    posibleYMax = [posibleYMax f(solDiff(i))];
  end
  xMax = solve(fsym==max(posibleYMax),x)(0);

  % Calculando ax y la multiplicacion
  posibleDMax = [];
  mult = 1;
  for i=1:n
    posibleDMax = [posibleDMax derivadan(soporte(i))]
    mult = mult * (xMax-soporte(i));
  end
  ax = max(posibleDMax);

  % Calculo final
  cota = (1/((n+1)!))*ax*mult;

end